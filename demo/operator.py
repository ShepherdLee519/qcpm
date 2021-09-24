from functools import wraps

ops = [
    "cx q[2],q[4];",
    "h q[0];",
    "tdg q[12];"
]

def countDecorator(func):
    index = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal index
        r = func(*args, index = index, **kwargs)
        index += 1

        return r
    return wrapper

class Operator:
    def __init__(self, op_type, operands, index = 0):
        self.type = op_type
        self.operands =  self._solve_operands(operands.split(','))
        self.index = index

        print(self.index, self.type, self.operands)
    
    def _solve_operands(self, operands):
        # eg. 'q[12]' => 12
        return [int(''.join( operand.split('[')[1][:-1] ) )
                    for operand in operands]


for op in ops:
    opObj = Operator( *(op[:-1].split(' ')) )