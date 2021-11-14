from qcpm.preprocess import preprocess
from qcpm.optimization import optimizer
from qcpm.operator import Operator
from qcpm.common import timerDecorator


class Circuit:
    """ Circuit object creating by QASM file.

    Example:
        data: cx q[4],q[1]; t q[4]; t q[2]; h q[0]; ...
            => operators: [Operator, Operator ...] (eg. Operator: cx [4,1])
            => draft: ctth...(cx => c)
    """
    @timerDecorator(description='Init Circuit')
    def __init__(self, path):
        self.operators = []
        self.draft = ''

        self._load_circuit(path)

    def _load_circuit(self, path):
        """ init Circuit according to QASM file.

        load data from a QASM file. 
        Init self.operators and self.draft.

        Args:
            path: path of QASM file.
        """
        op_types = []

        ops = preprocess(path)
        # eg. ['OPENQASM 2.0;\n', 'include "qelib1.inc";\n', 'qreg q[4];\n', ...]
        self.header = next(ops)

        # for operator in ops:
        # for operator in reduction(ops):
        for operator in optimizer(ops):
            self.operators.append(operator)
            # cx = convert_type() => c
            op_types.append( Operator.convert_type(operator.type) )
        
        self.draft = ''.join(op_types)

    def update(self):
        """ using self.operators re-calculate self.draft

        using after mapping(execute) application.
        abandon the operator which has type: Operator.ABANDON

        """
        self.operators = list(
            filter(
                lambda op: op.type != Operator.ABANDON, 
                self.operators
            )
        ) # abandon operators which has type: Operator.ABANDON(like '_').

        op_types = []

        for operator in self.operators:
            op_types.append( Operator.convert_type(operator.type) )

        self.draft = ''.join(op_types)

    def __len__(self):
        return len(self.draft)
    
    def __getitem__(self, index):
        return self.operators[index]

    @property
    def QASM(self):
        """ return QASM code of this circuit.
        
        """
        code = ''.join(self.header)

        for op in self:
            code += op.output

        return code

    def save(self, path):
        """ save code of this circuit to path

        save self.QASM to file(given by path)

        Args:
            path: like ./circuit (default extension: .qasm)
        """
        with open(f'{path}.qasm', 'w') as file:
            file.write(self.QASM)