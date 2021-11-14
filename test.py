import sys

from qcpm import Mapper, Circuit

# redirect to log file
# f = open('log.txt', 'w')
# sys.stdout = f

pattern_path = './data/pattern.json'
# pattern_path = './data/pattern_subtitute.json'
# circuit_path = './data/example'
# circuit_path = './data/example_big'
# circuit_path = './data/example_reduction'
# circuit_path = './data/example_reduction_3'
# circuit_path = './data/example_reduction_4'
# circuit_path = './data/example_rz'
circuit_path = './data/example_substitute'
# circuit_path = './data/test'

mapper = Mapper(pattern_path)
circuit = Circuit(circuit_path)

print(circuit.QASM)
circuit.save('./circuit_after')

# print(len(circuit.draft))
# print(circuit.draft)
# mapper.execute(circuit)