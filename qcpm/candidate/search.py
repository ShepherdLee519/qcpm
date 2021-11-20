from qcpm.candidate.candidate import Candidate
from qcpm.candidate.simulation import Simulation
from qcpm.candidate.plan import Plan, Plans


##########################
#                        #
#      Log Functions     #
#                        #
##########################

def logger(searcher):
    """ print log data

    Args:
        searcher: [self] of Searcher instance
    Returns:
        log: contains log functions:
            => call like: log('targets')(targets)

    
    """
    logpath = 'plan.txt'
    logdata = ''

    def startFunc():
        nonlocal logdata

        logdata = '' # reset logdata
        s = 'Monte Carlo-based plan searching\n\n'
        s += '-' * 12 + '\n\n'

        logdata += s

    def targetsFunc(targets):
        nonlocal logdata

        s = f'Expansion: Candidates size: {len(targets)}\n\n'
        for target in targets:
            s += str(target)
            s += '\n'
        
        logdata += s

    def selectedFunc(target):
        nonlocal logdata

        # log:
        # ----------
        # Selected: Pos: [40, 42] xx => I
        # ... xchxcxccch ...
        # 
        s = f'\nSelected: {target}\n'
        s += '    ... '

        end = searcher.pos + searcher.WINDOW_SIZE
        if end > len(searcher.circuit):
            end = len(searcher.circuit)
        for i in range(searcher.pos, end):
            s += searcher.circuit.draft[i]
        s += ' ... \n'

        logdata += s

        # log:
        # ----------
        # target:    ^ ^
        #
        s = ' ' * (end - searcher.pos)
        s = list(s)
        for index in target.pos:
            s[index - searcher.pos] = '^'
        s = 'target: ' + ''.join(s) + '\n'
        s += '\n' + '-' * 10

        logdata += s + '\n\n'

    def planFunc(selected):
        nonlocal logdata

        s = 'Complete Plan: \n\n'
        plan = '\n'.join([str(candidate) for candidate in selected])
        s += plan + '\n'
        s += f'\nTotal Saving: {searcher.saving}\n\n'

        logdata += s

    def endFunc(toFile=False):
        if toFile:
            with open(logpath, 'w') as f:
                f.write(logdata)
        else:
            print(logdata)

    ##############################################

    def log(key):
        logs_dict = {
            'start': startFunc,
            'targets': targetsFunc,
            'selected': selectedFunc,
            'plan': planFunc,
            'end': endFunc
        }

        return logs_dict[key]

    return log

############################
#                          #
#     Class Definition     #
#                          #
############################

class SearchPlan:
    """ Monte Carlo-based plan searching
    
    callable class:
        searchPlan(circuit, candidates)() => return Plans.

    Remember: after selecting each candidate:
        => candidate.apply(circuit); circuit.update()
    
    """
    WINDOW_SIZE = 20
    SIMULATION_SIZE = 10
    SIMULATION_TIMES = 10

    def __init__(self, circuit, candidates):
        """
        Args:
            circuit: Circuit object.
                    =>
                operators / draft.
            candidates: sorted list of Candidate object.
                    =>
                pos: eg. [1, 4]
                pattern: eg. pattern.src/dst => {'operator': 'xx', 'operands': 'aa'}
        """
        self.circuit = circuit
        self.candidates = candidates

        self.log = logger(self)

    def expansion(self):
        """ Expanase to get targte candidates

        Expanase target candidates at position self.cur
            => will change self.cur

        Returns:
            targets: list of Candidates with conflict from [self.cur]
        """ 
        while True:
            # ignore the after candidates that 
            # conflict with current selected candidates
            if self.candidates[self.cur] & self.selected:
                self.cur += 1
            else:
                break

        # current candidate => candidates[self.cur]
        targets = [ self.candidates[self.cur] ]

        # gather the candidates that have conflicts with current candidate.
        #   => self.candidates[i] & targets[0]
        for i in range(self.cur + 1, len(self.candidates)):
            if self.candidates[i] & targets[0]:
                targets.append(self.candidates[i])
            else:
                break
        
        self.cur += len(targets)

        return targets
    
    def simulation(self, candidates):
        """ simulation to evaluate value of each candidate.

        Args:
            candidates: list of Candidate object.
        -------
        Returns:
            values: list of int value
        """
        return [ Simulation(self)(candidate) + candidate.delta 
                    for candidate in candidates ]
    
    def reset(self):
        """ reset searcher's states

        """
        # candidates' cur
        ## will change after self.expansion
        self.cur = 0
        # operator position in circuit
        ## will change at Step 3 in __call__
        self.pos = 0

        # will change at Step 3 in __call__
        self.saving = 0 # total saving for selected plan
        self.selected = [] # should contains all selected candidates

    def __call__(self):
        """
        Returns:
            Plans object contains all possible plan.
        """
        self.reset() # reset searcher's state

        self.log('start')()
        while self.cur < len(self.candidates):
            # Step 1. select and expansion candidates
            targets = self.expansion()
            self.log('targets')(targets)

            # Step 2. Select and apply candidate
            ## if no conflict => apply candidate
            if len(targets) == 1:
                target = targets[0]
            ## else candidates with conflict => simulate
            else:
                values = self.simulation(targets)
                # choose the target with max value
                target = targets[ values.index(max(values)) ]
            self.pos = target.begin
            self.log('selected')(target)

            # Step 3. Apply selected candidate
            ## append selected candidate to self.selected
            ## real call will delay to self.plans.best().apply(circuit) in mapper
            self.selected.append(target)
            self.saving += target.delta
            self.pos = target.end + 1

        self.log('plan')(self.selected)
        self.log('end')()

        return Plans([ Plan(self.selected, self.saving) ])