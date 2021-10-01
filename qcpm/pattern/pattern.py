import string

from qcpm.operator import convert_type
from qcpm.common import countDecorator


@countDecorator
class Pattern:
    def __init__(self, src, dst, index=0):
        # eg. {'operaror': 'ccc', 'operands': 'abbcab'}
        self.index = index
        self.src = self._solve_pattern(src)
        self.dst = self._solve_pattern(dst)
        self.description = self._description(src, dst)
    
    def _description(self, src, dst):
        return 'Pattern: ' + str(self.index + 1) + '\n' \
                + '\n'.join(['\t' + op[0] + ' ' + str(op[1]) for op in src]) \
                + "\n\t => \n" \
                + ('\n'.join(['\t' + op[0] + ' ' + str(op[1]) for op in dst]) or '\tI')

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

    def delta(self):
        return len(self.src['operands']) - len(self.dst['operands'])