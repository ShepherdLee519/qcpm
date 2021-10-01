class Candidate:
    def __init__(self, pos, operator, pattern):
        self.pos = pos
        self.size = len(operator)
        self.end = pos + self.size - 1

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
            return self.pos + self.size - 1 >= other.pos