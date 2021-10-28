import string
from collections import deque

from qcpm.pattern import PatternMeta
from qcpm.operator import count_qubits, Operator, convert_type


def gatherTypes(ops):
    """
    :param ops: [Operator('h'), Operator('cx'),...] Operators
    :returns: 'hc...'
    """
    return ''.join(convert_type(op.type) for op in ops)

def matchTypes(opstr, pattern):
    """
    :param opstr: 'cchsh'
    :param pattern: 'hsh'
    :returns: match True, else False
    """
    size = len(pattern)
    if len(opstr) < size:
        return False
    else:
        return opstr[-size:] == pattern

######################## Class ########################

class ReductionPattern(PatternMeta):
    def __init__(self, src, dst):
        # self.src/dst = eg. {'operaror': 'ccc', 'operands': 'abbcab'}
        super().__init__(src, dst)

        self.size = len(self.src['operator'])

    def _matchTypes(self, ops):
        opstr = gatherTypes(ops)

        return matchTypes(opstr, self.src['operator'])

    def _matchOperands(self, ops):
        # eg. operands: abbc  
        #     targets:  [4, 1, 1, 2] 
        targets = [ operand for i in range(self.size)
                            for operand in ops[len(ops) - self.size + i].operands] 

        books = {k:-1 for k in string.ascii_lowercase}
        src_operands = self.src['operands']

        for i, operand in enumerate(src_operands):
            if books[operand] == -1:
                books[operand] = targets[i]
            elif books[operand] != targets[i]:
                return False, None
        
        return True, books

    def map(self, ops):
        if not self._matchTypes(ops):
            return False

        # Step 1. test operands matching
        # -----------------------------
        ok, books = self._matchOperands(ops)
        if not ok:
            return False

        # Step 2. pop old ops
        # ------------------------------
        # hscSh => Scs
        # operands: aabaaa => abaa
        # books: books[a] = 0, books[b] = 1
        for i in range(self.size):
            ops.pop()

        # Step 3. append new operator
        # ------------------------------
        j = 0
        dst_operator, dst_operands = self.dst['operator'], self.dst['operands']

        for i, operator in enumerate(dst_operator):
            operands_size = count_qubits(operator)
            operands = [ books[dst_operands[j + k]] for k in range(operands_size) ]
            ops.append( Operator(convert_type(operator, True), operands) )

            j += operands_size


class CommutationPattern(ReductionPattern):
    def __init__(self, src, dst):
        # self.src/dst = eg. {'operaror': 'ccc', 'operands': 'abbcab'}
        super().__init__(src, dst)

    def map(self, ops):
        if not self._matchTypes(ops):
            return False

        # Step 1. test operands matching
        # -----------------------------
        ok, _ = self._matchOperands(ops)
        if not ok:
            return False

        # Step 2. commutate
        temp = deque()
        for i in range(self.size):
            temp.append(ops.pop())

        for i in range(self.size):
            ops.append(temp.popleft())