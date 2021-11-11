from itertools import zip_longest

from qcpm.operator import Operator


class Candidate:
    """ Candidate object that contains mapped gates' positions etc.

    called in Mapper.execute( => find )

    """
    def __init__(self, pos, pattern):
        """
        Args:
            pos: eg. [1, 4]
            pattern: corresponding pattern like:
                pattern.src/dst => {'operator': 'xx', 'operands': 'aa'}
        """
        self.pos = pos
        self.size = len(pos)
        
        self.begin = pos[0]
        self.end = pos[-1]

        # Pattern.src / Pattern.dst => {'operator': 'xx', 'operands': 'aa'}
        # 
        # Pattern.opr = ['xcx', 'c']
        # Pattern.opd = ['aaba', 'ab']
        self.pattern = pattern # Pattern object

    def __repr__(self):
        dst = self.pattern.opr[1]
        if dst == '':
            dst = 'I'
        
        return f"Pos: {self.pos} {self.pattern.opr[0]} => {dst}"

    def __and__(self, other):
        """ check whether self(Candidate) conflicts with other

        Args:
            other: should be another Candidate object.
                but directly input positions list is also allowed.
        -------
        Example:
            Candidate1 & Candidate2 == True
                => conflict existing.
        """
        if other is None:
            return False
        else:
            try:
                return len(set(self.pos) & set(other.pos)) != 0
            except:
                # assume other is positions list
                return len(set(self.pos) & set(other)) != 0
    
    def apply(self, circuit):
        """ apply this candidated-mapping in the Circuit.

        called by Mapper.execute => Plans.apply

        Args:
            circuit: Circuit object
        """
        # example 1:
        # --------------------
        # self.pos: eg. [1, 6]
        # self.pattern.src: eg. {'operator': 'cc', 'operands': 'abab'}
        # self.pattern.dst: eg. {'operator': '', 'operands': ''}
        # 
        # example 2:
        # --------------------
        # self.pos: eg. [4, 5]
        # self.pattern.src: eg. {'operator': 'cc', 'operands': 'abbc'}
        # self.pattern.dst: eg. {'operator': 'c', 'operands': 'ac'}
        #
        _, books = self.pattern.match(circuit, self.pos, return_='books')

        cur = 0
        ops_from, ops_to = self.pattern.opr
        operands_to = self.pattern.dst['operands']

        print('Apply: ', self.__repr__())

        for i, (op_from, op_to) in enumerate(zip_longest(ops_from, ops_to)):
            # eg. h => 1, c => 2 ...
            size = Operator.count_qubits(op_from)
            # eg. 'ab' => [1, 4]
            operands = [ books[operand] for operand in operands_to[cur: cur + size] ]

            if op_to == None:
                op_to = Operator.ABANDON
            
            # apply => change this operator in circuit.
            circuit[self.pos[i]].change(
                op_to, # new operator
                operands
            )

            cur += size