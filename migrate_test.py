from qcpm import Circuit
from qcpm.migration import migrate

circuit_path = './data/test'
circuit = Circuit(circuit_path)

transfered = list(migrate(circuit, 'IBM', 'Surface'))
print(transfered)