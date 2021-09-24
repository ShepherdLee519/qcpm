import sys
sys.path.append('..')


# from qcpm.operator.operator import Operator
from qcpm.preprocess.preprocess import preprocess


class Circuit:
    def __init__(self, path):
        self.operators = []
        self.draft = ''
        self._load_circuit(path)

    def _load_circuit(self, path):
        op_types = []

        for operator in preprocess(path):
            self.operators.append(operator)
            op_types.append(operator.type)
        
        self.draft = ''.join(op_types)

circuit = Circuit('../data/example')
print(circuit.draft)
