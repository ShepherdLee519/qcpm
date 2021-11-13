from qcpm.candidate.simulation import Simulation
from qcpm.candidate.plan import Plan, Plans


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

        self.cur = 0 # candidates' cur
        self.pos = 0 # operator position in circuit

    def expansion(self):
        """ Expanase to get targte candidates

        Expanase target candidates at position self.cur
            => will change self.cur & self.pos

        Returns:
            targets: list of Candidates with conflict from [self.cur]
        """ 
        while True:
            if self.candidates[self.cur] & self.applied:
                self.cur += 1
            else:
                break

        targets = [ self.candidates[self.cur] ]
        for i in range(self.cur + 1, len(self.candidates)):
            # no conflict.
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
    
    def log(self, key):
        def startFunc():
            self.logdata = ''

            s = 'Monte Carlo-based plan searching\n\n'
            s += '-' * 12
            s += '\n\n'

            self.logdata += s

        def targetsFunc(targets):
            s = f'Expansion: Candidates size: {len(targets)}\n\n'

            for target in targets:
                s += str(target)
                s += '\n'
            
            self.logdata += s

        def selectedFunc(target):
            s = f'\nSelected: {target}\n'
            s += '    ... '

            end = self.pos + self.WINDOW_SIZE
            if end > len(self.circuit):
                end = len(self.circuit)
            for i in range(self.pos, end):
                s += self.circuit.draft[i]
            s += ' ... \n'

            s2 = ' ' * (end - self.pos)
            s2 = list(s2)
            for index in target.pos:
                s2[index - self.pos] = '^'
            s2 = 'target: ' + ''.join(s2) + '\n'
            s2 += '\n' + '-' * 10

            self.logdata += s + s2 + '\n\n'

        def planFunc(plan):
            s = 'Complete Plan: \n\n'
            s += str(plan) + '\n'
            s += f'\nTotal Saving: {self.saving}\n\n'

            self.logdata += s

        def endFunc():
            with open('plan.txt', 'w') as f:
                f.write(self.logdata)

    
        logs = {
            'start': startFunc,
            'targets': targetsFunc,
            'selected': selectedFunc,
            'plan': planFunc,
            'end': endFunc
        }

        return logs[key]

    def __call__(self):
        """
        Returns:
            Plans object contains all possible plan.
        """
        # print(self.candidates)
        
        # reset datas
        self.cur = 0
        self.pos = 0
        self.saving = 0
        self.applied = []
        # plan = ''

        # self.log('start')()
        while self.cur < len(self.candidates):
            # Step 1. select and expansion candidates
            targets = self.expansion()
            # self.log('targets')(targets)

            # Select and apply candidate
            ## Step 2.1 no conflict => apply candidate
            if len(targets) == 1:
                target = targets[0]
            ## Step 2.2 candidates with conflict => simulate
            else:
                # self.logdata += '\nSimulation: \n\n'
                values = self.simulation(targets)
                target = targets[ values.index(max(values)) ]

            self.pos = target.begin

            # self.log('selected')(target)

            ## Apply selected candidate
            self.applied.append(target)
            # plan += str(target) + '\n'
            self.saving += target.delta
            self.pos = target.end + 1

        # self.log('plan')(plan)
        # self.log('end')()

        return Plans([Plan(self.applied, self.saving)])