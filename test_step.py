from qcpm import Mapper, Circuit


circuit_path = './data/mult_after_light.qasm'


# Step 1. init mapper: eg. mapper = Mapper()
mapper = Mapper()


# Step 2. load and init Circuit: eg. circuit = Circuit(path)
"""
    params:
        - optimize: Whether to optimize, default: True
        - system: input format, "IBM" or "Surface"
"""
circuit = Circuit(circuit_path)



# Step 3. execute map on circuit: mapper.execute(circuit)
"""
    params:
        - stratrgy: strategy use to generate mapping plan, "MCM"/"random"
            default(None) greedy search.
        - metric: cycle / depth used to calculate value of candidate.
                default [cycle]
"""
mapper.execute(circuit, strategy='MCM', metric='cycle')


# Step 4. save results to qasm file: cricuit.save(save_path)
"""
    params:
        - system: output format, "IBM" or "Surface"
"""
circuit.save('./circuit_after')