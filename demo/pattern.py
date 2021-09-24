import json
import string
import sys
sys.path.append('..')


# from qcpm.operator.operator import Operator
# from qcpm.operator.convert import convert_type
from qcpm.pattern.mapper import Mapper

target = '../data/pattern.json'

    
# class Pattern:
#     def __init__(self, src, dst):
#         self.src = self._solve_pattern(src)
#         self.dst = self._solve_pattern(dst)

#         print(self.src, self.dst)
    
#     def _solve_pattern(self, target):
#         operator_pattern = [convert_type(operation[0]) for operation in target]
#         operands_pattern = [  string.ascii_lowercase[int(operands)] 
#             for operation in target for operands in operation[1]]

#         return {
#             "operaror": ''.join(operator_pattern),
#             "operands": ''.join(operands_pattern)
#         }

# class Mapper:
#     def __init__(self, path):
#         self.patterns = []
#         self._init_patterns(path)

#         # print(self.patterns)
        
#     def _init_patterns(self, path):
#         with open(path, 'r') as file:
#             patterns_data = json.load(file)

#             for pattern in patterns_data:
#                 self.patterns.append( Pattern(**pattern) )

mapper = Mapper(target)