import json
import string
from operator import attrgetter

from qcpm.pattern.pattern import Pattern
from qcpm.candidate import Candidate, filter
from qcpm.searcher import KMP

from qcpm.common import config
from qcpm.common import timerDecorator, Timer
from qcpm.common import title


class Mapper:

    @timerDecorator(description='Init Mapper')
    def __init__(self, path, searcher=KMP()):
        self.patterns = []
        self.plans = [] # candidates mapping plan

        self._candidates = []
        self._init_patterns(path)

        # search algorithm - default: KMP
        config['test'] and print(searcher)
        self.searcher = searcher
        
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
    
    def _validate(self, circuit, pos, operator, operands):
        # eg. operands: abbc  
        #     targets:  [4, 1, 1, 2] 
        targets = [ operand for i in range(len(operator))
                            for operand in circuit.operators[pos + i].operands] 

        books = {k:-1 for k in string.ascii_lowercase}

        for i, operand in enumerate(operands):
            if books[operand] == -1:
                books[operand] = targets[i]
            elif books[operand] != targets[i]:
                return False

        return True


    def find(self, circuit, pattern):
        operator, operands = pattern.src['operator'], pattern.src['operands']
        positions = self.searcher.apply(circuit.draft, operator)
        
        candidates_positions = []
        for pos in positions:
            if self._validate(circuit, pos, operator, operands):
                # operator: eg. cc operands: eg. abab
                candidates_positions.append(pos)
                self._candidates.append(Candidate(pos, operator, pattern))

                config['test'] and print("\npos: ", pos)
                config['test'] and circuit.print(pos, len(operator))
        
        config['test'] and print("\nCandidates: \n", candidates_positions)
        

    @timerDecorator(description='Execute Mapping')
    def execute(self, circuit):
        # 0. reset
        self._candidates = []

        # 1. collect possible candidates
        config['test'] and print('\n' + title('Pattern & Candidates'))
        with Timer('Find Candidates'):
            for i, pattern in enumerate(self.patterns):
                config['test'] and print('\n' + '-' * 12 + str(i + 1) + '-' * 12)
                config['test'] and print(pattern.description)

                self.find(circuit, pattern)

        # 2. filter candidates => (without conflict)
        with Timer('Filter Candidates'):
            self._candidates.sort(key=attrgetter('pos', 'size'))
            self.plans = filter(self._candidates)

            config['test'] and print('\n' + title('Candidate Plans') + '\n')
            config['test'] and print(self.plans)
        