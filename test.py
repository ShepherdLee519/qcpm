from qcpm import Mapper, Circuit, QCPatternMapper
from qcpm.circuit.info import CircuitInfo

pattern_path = './data/pattern.json'
# pattern_path = './data/pattern_subtitute.json'

# circuit_path = './data/example'
# circuit_path = './data/example_reduction'
# circuit_path = './data/example_reduction_3'
# circuit_path = './data/example_reduction_4'
circuit_path = './data/example_rz'
# circuit_path = './data/example_substitute'
# circuit_path = './BIGD/20QBT_45CYC_.7D1_.1D2_9.qasm' # 600
# circuit_path = './BIGD/20QBT_45CYC_.2D1_.4D2_4.qasm' # 300
# circuit_path = './BIGD/20QBT_45CYC_.2D1_.1D2_7.qasm' # 200
# circuit_path = './BIGD/20QBT_45CYC_.0D1_.2D2_0.qasm' # 100
# circuit_path = './data/test'



mapper = Mapper()
# mapper = Mapper(pattern_path)
circuit = Circuit(circuit_path)
# circuit = Circuit(circuit_path, optimize=False)
# circuitInfo = CircuitInfo(circuit)
# circuit.optimize()

# mapper.execute(circuit)
# mapper.execute(circuit, strategy='MCM')
# print(circuitInfo)
# print(CircuitInfo.compute_depth(circuit, detail=True))
# circuit.save('./circuit_after')



# QCPM = QCPatternMapper(log='./log.txt')
QCPM = QCPatternMapper()

# solve single qasm file
# QCPM.execute(circuit_path, './circuit_after')
# QCPM.execute(circuit_path, './circuit_after', silence=True)
QCPM.execute(circuit_path, strategy='MCM')
# QCPM.execute(circuit_path)
# QCPM.execute(circuit_path, './circuit_after', strategy='MCM')

# input_dir / output_dir
# QCPM.execute('./data/', './output/', strategy='MCM')
# QCPM.execute('./BIGD/', './BIGD_output', strategy='MCM')