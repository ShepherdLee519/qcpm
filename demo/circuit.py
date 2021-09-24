import sys
sys.path.append('..')


# from qcpm.preprocess.preprocess import preprocess
from qcpm.circuit.circuit import Circuit


# class Circuit:
#     def __init__(self, path):
#         self.operators = []
#         self.draft = ''
#         self._load_circuit(path)

#     def _load_circuit(self, path):
#         op_types = []

#         for operator in preprocess(path):
#             self.operators.append(operator)
#             op_types.append(operator.type)
        
#         self.draft = ''.join(op_types)

circuit = Circuit('../data/example2')
print(circuit.draft)
