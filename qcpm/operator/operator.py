from qcpm.common import countDecorator
from qcpm.operator.mixin import operatorMixin


class Operator(operatorMixin):
    """ Operator object corresponding to a gate operator.

    Including op_type: like "cx", "h" ...
    and operands which give the corresponding operands' positions in circuit.
    
    - op_type = '_' means this operator should be removed.
    - operands should always be a list. 

    Example:
        input: 'cx q[2],q[4]' 
            => self.type = 'cx', self.operands = [2, 4]
    """

    ABANDON = '_'
    reject_type = {'qreg', 'creg'}

    @countDecorator
    def __init__(self, op_type, operands, index = 0):
        """
        Args:
            op_type: like "cx", input is the type before converting.
            operands: 
                1. read from QASM: "q[2],q[4]"
                2. deirectly input a list: [2, 4]
        """
        if op_type in self.reject_type:
            raise ValueError(f"value <{op_type}> doesn't mean a operator")

        self.type = self._rotate_filter(op_type)
        self.angle = ''
        self.index = index
        
        if isinstance(operands, list):
            # directly input list like: [1, 4]
            self.operands = operands
        else:
            # operands is str like "q[2],q[4]"
            self.operands =  self._solve_operands(operands)    

    def _rotate_filter(self, op_type):
        """ 
        if operator is a rotate Gate, solve to save the angle.

        """
        if op_type[:1] == 'r': # eg. rz
            self.angle = op_type[3:][:-1]

            # op_type[:2] => eg. 'rz'
            return self.convert_type(op_type[:2])
        else:
            return op_type
    
    def _solve_operands(self, operands):
        """ solve operands(str) input.

        Args:
            operands: like "q[2],q[4]"
        -------
        Example:
            "q[2],q[4]" => ["q[2]", "q[4]"]
                        => [2, 4] (return)
        """
        operands = operands.split(',')

        return [int(''.join( operand.split('[')[1][:-1] ) )
                    for operand in operands]

    def change(self, new_type, new_operands=None):
        """ change info about operator manually

        Args:
            new_type: '_' means to abandon this operator.
                otherwise new_type should be a type before converting, like 'cx'
            new_operands: default: keep the setted operands.
        """
        self.type = new_type

        if new_operands != None:
            self.operands = new_operands
        
        return self

    def __repr__(self):
        return "No: {}, {} {}".format(self.index, self.type, self.operands)