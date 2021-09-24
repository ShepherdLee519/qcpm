import json
import string

from qcpm.pattern.pattern import Pattern
from qcpm.searcher.kmp import KMP


class Mapper:
    def __init__(self, path, searcher=KMP()):
        self.patterns = []
        self._init_patterns(path)
        self.searcher = searcher
        
    def _init_patterns(self, path):
        with open(path, 'r') as file:
            patterns_data = json.load(file)

            for pattern in patterns_data:
                self.patterns.append( Pattern(**pattern) )
    
    def _validate(self, circuit, pos, operator, operands):
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
        positions = self.searcher.apply(
            circuit.draft, operator)
        
        candidate = []
        for pos in positions:
            if self._validate(circuit, pos, operator, operands):
                candidate.append(pos)

                print("\npos: ", pos)
                circuit.print(pos, len(operator))
        
        print("\nCandidate: \n", candidate)
        

    def execute(self, circuit):
        for i, pattern in enumerate(self.patterns):
            print("\nPattern: ", i + 1)

            self.find(circuit, pattern)