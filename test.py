import sys

from qcpm.pattern.mapper import Mapper
from qcpm.circuit.circuit import Circuit

# redirect to log file
f = open('log.txt', 'w')
sys.stdout = f

pattern_path = './data/pattern.json'
circuit_path = './data/example'

mapper = Mapper(pattern_path)
circuit = Circuit(circuit_path)

mapper.execute(circuit)