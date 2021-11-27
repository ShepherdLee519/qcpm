from qcpm import Circuit

circuit_path = './data/example_test_migration'
# circuit_path = './data/test'
circuit = Circuit(circuit_path, optimize=False)

circuit.save('circuit_after', to='Surface')