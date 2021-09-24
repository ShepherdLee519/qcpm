import sys
from timer import Timer

from qcpm.pattern.mapper import Mapper
from qcpm.circuit.circuit import Circuit

# redirect to log file
f = open('log.txt', 'w')
sys.stdout = f

pattern_path = './data/pattern.json'
circuit_path = './data/example'

timer = Timer()
timer.start('init mapper')
mapper = Mapper(pattern_path)
timer.end()

timer.start('init circuit')
circuit = Circuit(circuit_path)
timer.end()

timer.start('execute mapper')
mapper.execute(circuit)
timer.end()