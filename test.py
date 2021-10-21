import sys

from qcpm import Mapper, Circuit, config

config['test'] = True

# redirect to log file
# f = open('log.txt', 'w')
# sys.stdout = f

# pattern_path = './data/pattern.json'
# circuit_path = './data/example'
circuit_path = './data/example_reduction'

# mapper = Mapper(pattern_path)
circuit = Circuit(circuit_path)
print(len(circuit.draft))
# print(circuit.operators)
# mapper.execute(circuit)