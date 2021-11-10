import string
from itertools import zip_longest

from qcpm.operator import count_qubits


class Candidate:
    def __init__(self, pos, operator, pattern):
        self.pos = pos
        self.size = len(pos)
        
        self.begin = pos[0]
        self.end = pos[-1]

        self.operator = operator
        # pattern.src/dst => {'operator': 'xx', 'operands': 'aa'}
        self.pattern = pattern

    def __repr__(self):
        dst = self.pattern.dst['operator']
        if dst == '':
            dst = 'I'
        
        return "Pos: {} {} => {}".format(self.pos, self.operator, dst)

    def __and__(self, other):
        """
            return True => self conflict with other
        """
        if other is None:
            return False
        else:
            try:
                return len(set(self.pos) & set(other.pos)) != 0
            except:
                return len(set(self.pos) & set(other)) != 0
    
    def apply(self, circuit):
        # example 1:
        # --------------------
        # self.pos: eg. [1, 6]
        # self.operator: eg. cc
        # self.pattern.src: eg. {'operator': 'cc', 'operands': 'abab'}
        # self.pattern.dst: eg. {'operator': '', 'operands': ''}
        # 
        # example 2:
        # --------------------
        # self.pos: eg. [4, 5]
        # self.operator: eg. cc
        # self.pattern.src: eg. {'operator': 'cc', 'operands': 'abbc'}
        # self.pattern.dst: eg. {'operator': 'c', 'operands': 'ac'}
        # 

        # print(self.pos)
        # print(self.operator)
        # print(self.pattern.src)
        # print(self.pattern.dst)

        books = {k:-1 for k in string.ascii_lowercase}

        targets = [ operand for i in range(self.size)
                            for operand in circuit.operators[self.pos[i]].operands ]

        for i, operand in enumerate(self.pattern.src['operands']):
            if books[operand] == -1:
                books[operand] = targets[i]

        cur = 0
        ops_from, ops_to = self.pattern.src['operator'], self.pattern.dst['operator']
        operands_to = self.pattern.dst['operands']

        print('Apply: ', self.__repr__())

        for i, (op_from, op_to) in enumerate(zip_longest(ops_from, ops_to)):
            size = count_qubits(op_from)
            operands = [books[operand] for operand in operands_to[cur: cur + size]]

            # print(op_from, op_to)
            # print(operands)

            if op_to == None:
                op_to = '_'
            
            circuit.operators[self.pos[i]].change(
                op_to, # new operator
                operands
            )

            cur += size