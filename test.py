from qcpm import Mapper, Circuit, QCPatternMapper

pattern_path = './data/pattern.json'
# pattern_path = './data/pattern_subtitute.json'
# circuit_path = './data/example'
# circuit_path = './data/example_big'
# circuit_path = './data/example_reduction'
# circuit_path = './data/example_reduction_3'
# circuit_path = './data/example_reduction_4'
# circuit_path = './data/example_rz'
# circuit_path = './data/example_substitute'
circuit_path = './data/test'

# mapper = Mapper(pattern_path)
# circuit = Circuit(circuit_path)
# mapper.execute(circuit)
# circuit.save('./circuit_after')

# QCPM = QCPatternMapper(pattern_path, log='./log.txt')
QCPM = QCPatternMapper(pattern_path)
QCPM.execute(circuit_path, './circuit_after')