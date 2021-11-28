from qcpm.operator import Operator


class CircuitInfo:
    """ represent Circuit's detail info

    used in mapper when show result info.

    Example:
        circuit: h-z-h-h-x-h-s-h-h-h-h-cx-h-h-z-x-h-s-c-sdg-h-z-h-sdg-cx-s-h
        size: 27, gates_group = [x, z, s, cx, sdg, h],
        qubits_num: 2, depth: 22, depth_detail = [20, 22]

    """
    def __init__(self, operators):
        self.size = len(operators)
        
        self.circuit = ''
        self.gates_group = []
        self.qubits_num = 0
        # circuit/gates_group/qubtis_num will be set in _solve()
        self._solve(operators)

        # eg. depth_detail = [20, 22, -1, -1 ...] , qubits_num = 2
        #   => depth_detail = [20, 22] => depth = max(..) = 22
        self.depth_detail = self.compute_depth(operators, detail=True)[:self.qubits_num]
        self.depth = max(self.depth_detail)
        
    def _solve(self, operators):
        """ Solve operators to init circuitInfo

        draft/gates_group/qubtis_num will be set in this.

        Args:
            operators: may be list of Operator or Circuit object(already mapped) 
        """
        op_types = []
        qubits = set() # gather qubits index to count qubtis num
        gates = set() # gather all the operator occured

        # solve each operator
        for operator in operators:
            # op_type: cx / h ...
            op_type = operator.type

            op_types.append(op_type)
            gates.add(op_type)
            qubits = qubits | set(operator.operands)
        
        self.gates_group = list(gates)
        self.qubits_num = len(qubits)
        self.circuit = '-'.join(op_types)

    ##########################
    #                        #
    #     Static Methods     #
    #                        #
    ##########################

    @staticmethod
    def compute_depth(operators, *, detail=False):
        """ calculate depth of circuit

        Note that: 
            1. assume the max qubits size => MAX_QUBITS = 25
            2. depth count from 0
        
        Returns:
            max depth of each layers.
        """
        MAX_QUBITS = 25

        last_layer = [-1] * MAX_QUBITS

        for operator in operators:
            opds = operator.operands
            
            try:
                if len(opds) == 1:
                    # x q[3] => opds = [3] => depth of qubit 3 increase.
                    last_layer[ opds[0] ] += 1
                else:
                    # cx q[2], q[5] => opds = [2, 5]
                    # => depth of qubit 2, 5 become the bigger depth + 1
                    # for example:
                    # -------
                    # 2: ...xhhh depth: 10
                    # 5: ...xx   depth: 8
                    # 
                    # thus:
                    # 2: ...xhhhC depth: 11
                    # 5: ...xx  X depth: 11
                    layers = map(lambda opd: last_layer[opd], opds)
                    layer = max(layers) + 1

                    for opd in opds:
                        last_layer[opd] = layer
            except IndexError:
                print(f'Error occured during solving operator: <{opds}>')
                print(f'Qubits num is over the limit: <{MAX_QUBITS}>.')
                raise
        
        if detail:
            return last_layer
        else:
            return max(last_layer)

    @staticmethod
    def evaluate_depth(target):
        """ evaluate the depth of circuit

        depth <= 100 => small
        100 < depth < 1000 => medium
        depth >= 1000 => large

        Args:
            target: may be:
                => depth: depth of circuit.
                => circuit: Circuit object
        """
        if isinstance(target, int):
            depth = target
        else:
            depth = CircuitInfo.compute_depth(target)

        if depth <= 100:
            return 'small'
        elif depth < 1000:
            return 'medium'
        else:
            return 'large'

    ##########################
    #                        #
    #     Dunder Methods     #
    #                        #
    ##########################

    def __repr__(self):
        info = 'Circuit Info: \n'
        info += f' - circuit: {self.circuit} \n     => total size: [{self.size}]\n'
        info += ' ' + '-' * 20 + '\n'
        info += f' - qubits_num: {self.qubits_num}, using gates: [{",".join(self.gates_group)}]\n'
        info += f' - circuit depth: {self.depth} - ({self.evaluate_depth(self.depth)})\n'

        return info