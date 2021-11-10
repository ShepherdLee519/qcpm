import json
import string

from qcpm.candidate import Candidate, filterCandidates
from qcpm.pattern.pattern import Pattern
from qcpm.pattern.positioning import positioning

from qcpm.common import config
from qcpm.common import timerDecorator, Timer
from qcpm.common import title


class Mapper:

    @timerDecorator(description='Init Mapper')
    def __init__(self, path):
        self.patterns = []
        self.plans = [] # candidates mapping plan

        self._candidates = []
        self._init_patterns(path)
        
    def _init_patterns(self, path):
        with open(path, 'r') as file:
            patterns_data = json.load(file)

            # pattern: 
            # {
            #     "src": [ ["x", [1]], ["cx", [0, 1]], ["x", [1]] ],
            #     "dst": [ ["cx", [0, 1]] ]
            # }
            for pattern in patterns_data:
                # Pattern(src, dst)
                self.patterns.append( Pattern(**pattern) )

    def _validate(self, operands):

        def validate(position):
            # 1. Validate Operands
            # eg. operands: abbc  
            #     targets:  [4, 1, 1, 2] 
            targets = [ operand for i in range(len(position))
                                for operand in self.circuit.operators[position[i]].operands ]
            books = {k:-1 for k in string.ascii_lowercase}

            for i, operand in enumerate(operands):
                if books[operand] == -1:
                    books[operand] = targets[i]
                elif books[operand] != targets[i]:
                    return False

            # 2. Validate no conflicts
            targets = set(targets) # [4, 1, 1, 2] => {4, 1, 2}
            # eg. position: [4, 7, 10]
            # => check (4, 10) (without 7) that has no conflict with targets
            for pos in range(position[0] + 1, position[-1]):
                if pos not in position:
                    operand = self.circuit.operators[pos].operands
                    # eg. [control, *targets] => *targets
                    if len(operand) >= 2:
                        operand = operand[1:]

                    ops = set(operand)
                    
                    # eg. have no intersection => no conflict
                    if len(targets & ops) != 0:
                        return False

            return True
        
        return validate


    def find(self, pattern):
        # eg. operator: xcx , operands: babb
        operator, operands = pattern.src['operator'], pattern.src['operands']
        positions = positioning(self.circuit.draft, operator)
        # print(positions)

        validater = self._validate(operands)
        validated_positions = filter(validater, positions)

        config['test'] and print("\nCandidates: \n")
        for position in validated_positions:
            self._candidates.append(Candidate(position, operator, pattern))

            config['test'] and print(position)


    @timerDecorator(description='Execute Mapping')
    def execute(self, circuit):
        # 0. reset
        self.circuit = circuit
        self._candidates = []

        # 1. collect possible candidates
        config['test'] and print('\n' + title('Pattern & Candidates'))
        with Timer('Find Candidates'):
            for i, pattern in enumerate(self.patterns):
                config['test'] and print('\n' + '-' * 12 + str(i + 1) + '-' * 12)
                config['test'] and print(pattern.description)

                self.find(pattern)

        # 2. filter candidates => (without conflict)
        with Timer('Generate Plans'):
            self._candidates.sort(key=lambda x: (x.begin, x.size, x.end))
            print(self._candidates)

            # TODO:
            # should return a Plans object
            # self.plans = searchPlan(self._candidates)
            self.plans = filterCandidates(self._candidates)

            config['test'] and print('\n' + title('Generate Plans') + '\n')
            config['test'] and print(self.plans)
        
        # 3. apply the best plan
        with Timer('apply mapping plan'):
            config['test'] and print('\n' + title('Apply Mapping Plan') + '\n')

            self.plans[0].apply(circuit)
        