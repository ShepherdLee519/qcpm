import string

from qcpm.operator import Operator
from qcpm.common import countDecorator


class PatternMeta:
    # use Example:
    # operands: "abaa", targets: [1, 2, 1, 1]
    # => that means: books: {'a': 1, 'b': 2, 'c': -1, ...}
    books = {k:-1 for k in string.ascii_lowercase}

    def __init__(self, src, dst):
        """
        src/dst: 
        eg. [ ["x", [1]], ["cx", [0, 1]], ["x", [1]] ]

        self.src/self.dst:
        eg. {'operaror': 'xcx', 'operands': 'abaa'}
        
        """
        self.data = {
            'src': src,
            'dst': dst
        }

        self.src = self._solve_pattern(src)
        self.dst = self._solve_pattern(dst)

        self.opr = [ self.src['operator'], self.dst['operator'] ]
        self.opd = [ self.src['operands'], self.dst['operands'] ]
    
    def _solve_pattern(self, target):
        """
        eg. target:
        
        [ 
            ["x", [1]], 
            ["cx", [0, 1]], 
            ["x", [1]] 
        ],
        
        after _solve_pattern():
        
        {
            "operator": "xcx",
            "operands": "abaa"
        }
        
        """
        operator_pattern = [ Operator.convert_type(operation[0]) for operation in target ]
        operands_pattern = [ string.ascii_lowercase[int(operands)] 
            for operation in target for operands in operation[1] ]

        return {
            'operator': ''.join(operator_pattern),
            'operands': ''.join(operands_pattern)
        }
    
    def match(self, operators, positions, *, return_='targets'):
        """ match whether tagets operators(circuit) match this pattern

        Args:
            operators: container of operators, may be Circuit object.
            positions: positions need to check.
            return_: the extra object need to return.
        -------
        Returns:
            bool: True/False: whether mathed.
            extra_object:
                corresponding to return_, will be:

                    - 'targets': targets that contains operands indexes. (default)
                    - 'books': a map about letter to index. eg. 'a' => 1
                    - 'all': dict containes both targets and books. 
        """
        # reset books
        for k in self.books:
            self.books[k] = -1
        
        # eg. operands: abbc  
        #     targets:  [4, 1, 1, 2] 
        # 
        targets = [ operand for i in range(len(positions))
                            # circuit[index] => operator object,
                            # operator.operands => positions like [1, 4]
                            for operand in operators[positions[i]].operands ]
        
        for i, operand in enumerate(self.opd[0]):
            if self.books[operand] == -1:
                self.books[operand] = targets[i]
            elif self.books[operand] != targets[i]:
                return False, None

        # matched => select extra_obj to return
        if return_ == 'targets':
            extra_obj = targets
        elif return_ == 'books':
            extra_obj = self.books.copy()
        elif return_ == 'all':
            extra_obj = {
                'targets': targets,
                'books': self.books.copy()
            }

        return True, extra_obj
    

@countDecorator
class Pattern(PatternMeta):
    def __init__(self, src, dst, index=0):
        super().__init__(src, dst)

        self.index = index
    
    @property
    def delta(self):
        """ calculate cost saving.

        calculate delta cost-saving after using this pattern

        """
        # eg. opr = ['xcx', 'c']
        # delta: (1 + 2 + 1) - (2)
        return sum(map(Operator.count_qubits, list(self.opr[0]))) - \
            sum(map(Operator.count_qubits, list(self.opr[1])))

    def __repr__(self):
        INDENT = ' ' * 4

        return 'Pattern: ' + str(self.index + 1) + '\n' \
            + '\n'.join([INDENT + op[0] + ' ' + str(op[1]) for op in self.data['src']]) \
            + "\n" + INDENT + "=> \n" \
            + ('\n'.join([INDENT + op[0] + ' ' + str(op[1]) for op in self.data['dst']]) \
                or f'{INDENT}I')