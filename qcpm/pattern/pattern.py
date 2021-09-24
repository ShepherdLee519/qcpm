import string

from qcpm.operator.convert import convert_type
from qcpm.common.decorator import countDecorator


@countDecorator
class Pattern:
    def __init__(self, src, dst, index=0):
        # eg. {'operaror': 'ccc', 'operands': 'abbcab'}
        self.index = index
        self.src = self._solve_pattern(src)
        self.dst = self._solve_pattern(dst)
        self.description = '\n'.join([op[0] + ' ' + str(op[1]) for op in src]) \
                            + "\n => \n" \
                            + '\n'.join([op[0] + ' ' + str(op[1]) for op in dst]) 

        print("Pattern ", self.index + 1)
        print(self.description)
    
    def _solve_pattern(self, target):
        # eg. target:
        # {
        #     "src": [ ["x", [1]], ["cx", [0, 1]], ["x", [1]] ],
        #     "dst": [ ["cx", [0, 1]] ]
        # }
        operator_pattern = [convert_type(operation[0]) for operation in target]
        operands_pattern = [  string.ascii_lowercase[int(operands)] 
            for operation in target for operands in operation[1]]

        return {
            "operator": ''.join(operator_pattern),
            "operands": ''.join(operands_pattern)
        }