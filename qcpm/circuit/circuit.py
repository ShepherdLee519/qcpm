import os

from qcpm.preprocess import preprocess
from qcpm.optimization import optimizer, reduction
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
        self.origin = '' # origin circuit's gates string
        self.draft = '' # solved circuit's gates string

        self.optimize( self._load_circuit(path) )

    def _load_circuit(self, path):
        """ init Circuit according to QASM file.

        load data from a QASM file. 
        Init self.operators and self.draft.

        Args:
            path: path of QASM file.
        """
        op_types = []

        ops = preprocess(path) # iterator
        # eg. ['OPENQASM 2.0;\n', 'include "qelib1.inc";\n', 'qreg q[4];\n', ...]
        self.header = next(ops)

        for operator in ops:
            yield operator
            # cx = convert_type() => c
            op_types.append( Operator.convert_type(operator.type) )
        
        # keep the gates string of origin input circuit.
        self.origin = ''.join(op_types)

    def _optimize(self, operators, *, optimizer=optimizer):
        """ optimization during each turn

        using [optimizer] in ./optimization
            => Reduction -> Commutation

        Args:
            operators: iteratable Operators object.
            optimizer: optimizer using to optimize operators.
                => eg. qcpm.optimization.optimizer / qcpm.optimization.reduction
                => if None, just read in without optimization.
        -------
        Returns:
            changed[bool]:
                - True => will still call _optimize unless the turns of 
                    optimization is over the LIMIT.
                - False => Stop useless optimization. 
        """
        temp_operators = []
        op_types = []

        # get iterator of operators after optimization
        if optimizer == None:
            targets = operators
        else:
            targets = optimizer(operators)

        # solve each operator
        for operator in targets:
            temp_operators.append(operator)
            # cx = convert_type() => c
            op_types.append( Operator.convert_type(operator.type) )
        
        draft = ''.join(op_types)
        changed = draft != self.draft

        self.draft = draft
        # self.operators = temp_operators

        return changed, temp_operators
    
    def optimize(self, operators=None, *, iteration=3):
        """ Optimize the loaded circuit by each Operator until no change occurs

        using _optimize() while no change occurs.

        Args:
            operators: iteratable Operators object.
                => if operators is None, optimize circuit(self) itself.
            iteration: iteration turns that optimization. default=3
        """
        if operators == None:
            operators = self

        count = 0
        while count < iteration:
            # optimize: reduction -> commutation
            changed, operators = self._optimize(operators)

            if not changed:
                # after reduction -> commutation -> ... -> reduction -> commutation
                # at last: apply reduction.
                _, operators = self._optimize(operators, optimizer=reduction)
                break
            
            count += 1
        
        self.operators = operators

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

        # update circuit's draft representation.
        self.draft = ''.join(op_types)

    @property
    def QASM(self):
        """ return QASM code representation of this circuit.
        
        """
        # remember header: eg. ['OPENQASM 2.0;\n', ...]
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
        path = path + '.qasm' if os.path.splitext(path)[-1] == '' else path

        with open(path, 'w') as file:
            file.write(self.QASM)
        
    def __len__(self):
        # len(circuit) <=> len(circuit.draft)
        return len(self.draft)
    
    def __getitem__(self, index):
        # thus circuit[i] <=> circuit.operators[i]
        return self.operators[index]