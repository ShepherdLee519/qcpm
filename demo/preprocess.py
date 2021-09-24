import sys
sys.path.append('..')


from qcpm.operator.operator import Operator

target = '../data/example.qasm'

with open(target, 'rt') as file:
    # Skip the first two lines
    # Skip => OPENQASM 2.0; include "qelib1.inc"; 
    next(file)
    next(file)
    
    for line in file:
        # "cx q[2],q[4];" => 'cx', 'q[2],q[4]'
        op_type, operands = (line.strip()[:-1].split(' '))
        try:
            op = Operator(op_type, operands)
            # print(op)
        except ValueError:
            pass