from qcpm import Mapper, Circuit, QCPatternMapper
from qcpm.circuit.info import CircuitInfo

# circuit_path = './data/example'
# circuit_path = './BIGD/20QBT_45CYC_.7D1_.1D2_9.qasm' # 600
# circuit_path = './BIGD/20QBT_45CYC_.2D1_.4D2_4.qasm' # 300
# circuit_path = './BIGD/20QBT_45CYC_.2D1_.1D2_7.qasm' # 200
# circuit_path = './BIGD/20QBT_45CYC_.0D1_.2D2_0.qasm' # 100
circuit_path = './data/test'
# circuit_path = './data/test_surface'


# Step 1. init mapper: eg. mapper = Mapper()
# Step 2. load and init Circuit: eg. circuit = Circuit(path)
# Step 3. execute map on circuit: mapper.execute(circuit)
# Step 4. save results to qasm file: cricuit.save(save_path)
# 
# mapper = Mapper()
"""
    params:
        - optimize: Whether to optimize, default: True
        - system: input format, "IBM" or "Surface"
"""
# circuit = Circuit(circuit_path)
# circuit = Circuit(circuit_path, system='Surface')
# circuit = Circuit(circuit_path, optimize=False)

# mapper.execute(circuit)
# mapper.execute(circuit, strategy='MCM')

# circuit.save('./circuit_after')
# circuit.save('./circuit_after', system='Surface')



# QCPM = QCPatternMapper(log='./log.txt')
QCPM = QCPatternMapper()

# solve single qasm file
# QCPM.execute(circuit_path, './circuit_after')
QCPM.execute(circuit_path, './circuit_after', 
    strategy='MCM', system=['IBM', 'Surface'])
# QCPM.execute(circuit_path, './circuit_after', 
#     strategy='MCM', system='Surface')

# input_dir / output_dir
# QCPM.execute('./data/', './output/', strategy='MCM', system='IBM')
# QCPM.execute('./BIGD/', './BIGD_output', strategy='MCM')