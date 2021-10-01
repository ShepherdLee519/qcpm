import os

from qcpm.operator import Operator


def preprocess(path, ext='.qasm'):
    path = path + ext if os.path.splitext(path)[-1] == '' else path
    
    with open(path, 'rt') as file:
        # Skip the first two lines
        # Skip => OPENQASM 2.0; include "qelib1.inc"; 
        next(file)
        next(file)
        
        for line in file:
            # "cx q[2],q[4];" => 'cx', 'q[2],q[4]'
            op_type, operands = (line.strip()[:-1].split(' '))
            try:
                op = Operator(op_type, operands)
                yield op
                # print(op)
            except ValueError:
                pass