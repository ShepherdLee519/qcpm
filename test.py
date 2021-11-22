from qcpm import Mapper, Circuit, QCPatternMapper

pattern_path = './data/pattern.json'
# pattern_path = './data/pattern_subtitute.json'

# circuit_path = './data/example'
# circuit_path = './data/example_reduction'
# circuit_path = './data/example_reduction_3'
# circuit_path = './data/example_reduction_4'
# circuit_path = './data/example_rz'
# circuit_path = './data/example_substitute'
circuit_path = './data/test'



# mapper = Mapper()
# mapper = Mapper(pattern_path)
# circuit = Circuit(circuit_path)

# mapper.execute(circuit, strategy='MCM', silence=True)
# mapper.execute(circuit)
# circuit.optimize()
# circuit.save('./circuit_after')



# QCPM = QCPatternMapper(log='./log.txt')
QCPM = QCPatternMapper()

# solve single qasm file
# QCPM.execute(circuit_path, './circuit_after')
# QCPM.execute(circuit_path, './circuit_after', silence=True)
QCPM.execute(circuit_path, './circuit_after', strategy='MCM')
# QCPM.execute(circuit_path, './circuit_after', strategy='MCM', silence=True)

# input_dir / output_dir
# QCPM.execute('./data/', './output/', strategy='MCM')