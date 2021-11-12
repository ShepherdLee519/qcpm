from qcpm.candidate.simulation import Simulation
from qcpm.candidate.plan import Plan, Plans


class SearchPlan:
    """ Monte Carlo-based plan searching
    
    callable class:
        searchPlan(circuit, candidates)() => return Plans.

    Remember: after selecting each candidate:
        => candidate.apply(circuit); circuit.update()
    
    """
    WINDOW_SIZE = 15
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

    def __call__(self):
        """
        Returns:
            Plans object contains all possible plan.
        """
        # print(self.candidates)
        
        self.cur = 0
        self.pos = 0
        self.saving = 0
        self.applied = []
        plan = ''
        #########################################
        print('Monte Carlo-based plan searching')
        print('-' * 12)
        #########################################
        while self.cur < len(self.candidates):
            # Step 1. select and expansion candidates
            targets = self.expansion()

            #########################################
            print(f'Expansion: Candidates size: {len(targets)}\n')
            for target in targets:
                print(target)   
            #########################################

            # Select and apply candidate
            ## Step 2.1 no conflict => apply candidate
            if len(targets) == 1:
                target = targets[0]
            ## Step 2.2 candidates with conflict => simulate
            else:
                values = self.simulation(targets)
                target = targets[ values.index(max(values)) ]

            self.pos = target.begin

            #########################################
            print()
            print(f'Selected: {target}')
            s = '    ... '
            end = self.pos + self.WINDOW_SIZE
            if end > len(self.circuit):
                end = len(self.circuit)
            for i in range(self.pos, end):
                s += self.circuit.draft[i]
            s += ' ... '
            print(s)

            s = ' ' * (end - self.pos)
            s = list(s)
            for index in target.pos:
                s[index - self.pos] = '^'
            s = 'target: ' + ''.join(s)
            print(s)
            print()
            #########################################

            ## Apply selected candidate
            self.applied.append(target)
            plan += str(target) + '\n'
            self.saving += target.delta
            self.pos = target.end + 1

            print('-' * 10) 

        #########################################
        print('Complete Plan: \n')
        print(plan)
        print(f'\nTotal Saving: {self.saving}\n\n')
        #########################################

        return Plans([Plan(self.applied, self.saving)])