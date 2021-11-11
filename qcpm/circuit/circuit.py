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

        # for operator in preprocess(path):
        # for operator in reduction(preprocess(path)):
        for operator in optimizer(preprocess(path)):
            self.operators.append(operator)
            # cx = convert_type() => c
            op_types.append( Operator.convert_type(operator.type) )
        
        self.draft = ''.join(op_types)

    def update(self):
        """ using self.operators re-calculate self.draft

        using after mapping(execute) application.
        abandon the operator which has type: Operator.ABANDON

        """
        self.operators = filter(
            lambda op: op.type != Operator.ABANDON, 
            self.operators
        ) # abandon operators which has type: Operator.ABANDON(like '_').

        op_types = []

        for operator in self.operators:
            op_types.append( Operator.convert_type(operator.type) )

        self.draft = ''.join(op_types)

    def __len__(self):
        return len(self.draft)
    
    def __getitem__(self, index):
        return self.operators[index]