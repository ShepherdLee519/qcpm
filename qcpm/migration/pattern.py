from qcpm.optimization.pattern import ReductionPattern
from qcpm.operator import Operator


class MigrationPattern(ReductionPattern):
    def __init__(self, src, dst):
        # self.src/dst = eg. {'operaror': 'ccc', 'operands': 'abbcab', angles: [None, ...]}
        super().__init__(src, dst)

    def map(self, ops):
        if not self._matchTypes(ops):
            return []
        
        ok, books = self.match(
            ops,
            list( range( len(ops) - self.size, len(ops) ) ),
            return_ ='books'
        )

        if not ok:
            return []

        for i in range(self.size):
            ops.pop()

        cur = 0
        results = []
        # eg. dst_operator = 'xY', dst_operands = 'aa', dst_angles = [None, "-pi/2"]
        dst_operator, dst_operands, dst_angles = self.dst['operator'], self.dst['operands'], self.dst['angles']

        for i, operator in enumerate(dst_operator):
            # eg. operator = 'c' => operands_size = 2
            operands_size = Operator.count_qubits(operator)
            # if books = {'a': 1, 'b': 4, ...}
            # then operands "ab"  => [1, 4]
            operands = [ books[dst_operands[cur + k]] for k in range(operands_size) ]

            # Operator.op_type should be original type just like in QASM, eg. cx
            # Operator.convert_type(operator, True):
            #   => 'Y' => 'ry'
            op_type = Operator.convert_type(operator, True)
            if Operator.is_rotation(op_type):
                op_type = f'{op_type}({dst_angles[i]})'
            results.append( Operator(op_type, operands) )

            cur += operands_size
        
        return results
        
