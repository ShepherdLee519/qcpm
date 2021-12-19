from qcpm import Mapper, Circuit, QCPatternMapper, circuit
from qcpm.circuit.info import CircuitInfo

# circuit_path = './data/example'
# circuit_path = './data/example_reduction'
circuit_path = './benchmark/BIGD/20QBT_45CYC_.7D1_.1D2_9.qasm' # 600
# circuit_path = './BIGD/20QBT_45CYC_.2D1_.4D2_4.qasm' # 300
# circuit_path = './BIGD/20QBT_45CYC_.2D1_.1D2_7.qasm' # 200
# circuit_path = './BIGD/20QBT_45CYC_.0D1_.2D2_0.qasm' # 100
# circuit_path = './data/test'
# circuit_path = './data/test_surface'
# circuit_path = './depth_data/large_1.qasm'

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
# circuit = Circuit(circuit_path, system='IBM')
# circuit = Circuit(circuit_path, optimize=False)


# mapper.execute(circuit)
# mapper.execute(circuit, strategy='MCM', metric='cycle')
# mapper.execute(circuit, strategy='MCM', metric='depth')
# mapper.execute(circuit, strategy='random', metric='depth')
# mapper.result()

# circuit.save('./circuit_after')
# circuit.save('./circuit_after', system='Surface')



# QCPM = QCPatternMapper(log='./log.txt')
QCPM = QCPatternMapper()

# solve single qasm file
QCPM.execute(circuit_path, './circuit_after',  metric='depth')
# QCPM.execute(circuit_path, './circuit_after',  metric='depth', strategy='random')
# QCPM.execute(circuit_path, './circuit_after', 
#     strategy='MCM', system=['IBM', 'Surface'], metric='depth')
# QCPM.execute(circuit_path, './circuit_after', 
#     strategy='MCM', system=['Surface', 'IBM'], metric='cycle')
# QCPM.execute(circuit_path, './circuit_after', 
#     strategy='MCM', system='Surface')
# QCPM.execute(circuit_path, './circuit_after', 
#     strategy='MCM', system='IBM', metric='cycle')
# QCPM.execute(circuit_path, './circuit_after', 
#     strategy='MCM', system='IBM', metric='depth')

# input_dir / output_dir
# QCPM.execute('./data/', './output/', strategy='MCM', system='IBM')
# QCPM.execute('./BIGD/', './BIGD_output', strategy='MCM')

# config = {
#     # 'log': 'log.txt', # for single file
#     # 'logs': './logs/', # for files
#     'strategy': 'MCM',
#     'system': 'IBM', # ['IBM', 'Surface]
#     'depth_size': 'medium', # default all
#     'metric': 'cycle' # cycle or depth
# }

# QCPM.execute('./depth_data/', './depth_data_output/', **config)