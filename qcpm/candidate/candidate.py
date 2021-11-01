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