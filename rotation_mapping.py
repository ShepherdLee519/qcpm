from qcpm.operator.operator import Operator
from qcpm.pattern.pattern import PatternMeta

pa1 = {
    "src": [
        ["z", [0]],
        ["ry", [0], "pi/2"]
    ],
    "dst": [
        ["h", [0]]
    ]
}

operators = []
operators.append( Operator('z', 'q[1]') )
operators.append( Operator('ry(pi/2)', 'q[1]') )

positions = [0, 1]

pattern = PatternMeta( **pa1 )

print(pattern.match(operators, positions))