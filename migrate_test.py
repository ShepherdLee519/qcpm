# from qcpm import Circuit
from qcpm.migration import convert
import json

# circuit_path = './data/example_test_migration'
# circuit_path = './data/test'
# circuit = Circuit(circuit_path, optimize=False)

# circuit.save('circuit_after', to='Surface')

# patterns_path = './qcpm/optimization/rules/IBM/hadamard.json'
# patterns_path = './qcpm/optimization/rules/IBM/commutation.json'
# patterns_path = './qcpm/optimization/rules/IBM/reversible.json'
patterns_path = './qcpm/pattern/rules/IBM/pattern.json'
# patterns_path = './qcpm/expander/rules/IBM/expansion.json'
with open(patterns_path, 'r') as file:
    patterns = json.load(file)

# print(patterns)
# convert(patterns, 'Surface')

# convert(patterns, 'Surface')
# with open('./qcpm/optimization/rules/Surface/reversible.json', 'w') as file:
with open('./qcpm/pattern/rules/U/pattern.json', 'w') as file:
    json.dump(convert(patterns, 'U'), file)
