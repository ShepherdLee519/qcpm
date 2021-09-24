import sys
sys.path.append('..')


# from qcpm.preprocess.preprocess import preprocess
from qcpm.pattern.mapper import Mapper
from qcpm.circuit.circuit import Circuit

target = '../data/pattern.json'

mapper = Mapper(target)
circuit = Circuit('../data/example')
print('\n\n')
mapper.execute(circuit)