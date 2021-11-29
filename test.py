from qcpm import Mapper, Circuit, QCPatternMapper
from qcpm.circuit.info import CircuitInfo

# pattern_path = './data/pattern.json'
# pattern_path = './data/pattern_subtitute.json'

# circuit_path = './data/example'
# circuit_path = './data/example_reduction'
# circuit_path = './data/example_reduction_3'
# circuit_path = './data/example_reduction_4'
# circuit_path = './data/example_rz'
# circuit_path = './data/example_substitute'
# circuit_path = './BIGD/20QBT_45CYC_.7D1_.1D2_9.qasm' # 600
# circuit_path = './BIGD/20QBT_45CYC_.2D1_.4D2_4.qasm' # 300
# circuit_path = './BIGD/20QBT_45CYC_.2D1_.1D2_7.qasm' # 200
# circuit_path = './BIGD/20QBT_45CYC_.0D1_.2D2_0.qasm' # 100
circuit_path = './data/test'
# circuit_path = './data/test_surface'

mapper = Mapper()
# circuit = Circuit(circuit_path)
circuit = Circuit(circuit_path, system='Surface', optimize=False)
# circuit = Circuit(circuit_path, optimize=False)
# circuit.optimize()

# mapper.execute(circuit)
# mapper.execute(circuit, strategy='MCM')
# print(circuit.info)
# circuit.optimize()
# mapper.execute(circuit, strategy='MCM')
# circuit.optimize()
# mapper.execute(circuit, strategy='MCM')
# print(CircuitInfo(circuit))
# print(circuit.info)
# print(CircuitInfo.compute_depth(circuit, detail=True))
# circuit.save('./circuit_after')
# circuit.save('./circuit_after', to='Surface')
circuit.save('./circuit_after', to='IBM')
# circuit.save('./circuit_after_surface', to='Surface')



# QCPM = QCPatternMapper(log='./log.txt')
# QCPM = QCPatternMapper()

# solve single qasm file
# QCPM.execute(circuit_path, './circuit_after')
# QCPM.execute(circuit_path, './circuit_after', silence=True)
# QCPM.execute(circuit_path, strategy='MCM')
# QCPM.execute(circuit_path)
# QCPM.execute(circuit_path, './circuit_after', strategy='MCM')

# input_dir / output_dir
# QCPM.execute('./data/', './output/', strategy='MCM')
# QCPM.execute('./BIGD/', './BIGD_output', strategy='MCM')