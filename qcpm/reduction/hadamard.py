from qcpm.operator import convert_type, Operator
from qcpm.reduction.common import solveRules, gatherTypes, matchTypes, matchOperands


rules = [
    ['h', 'h'],
    ['h', 's', 'h'],
    ['h', 'sdg', 'h'],
    ['h', 'h', 'cx', 'h', 'h'],
    ['h', 's', 'cx', 'sdg', 'h'],
    ['h', 'sdg', 'cx', 's', 'h'],
]

rules = solveRules(rules)

def HadamardReduction(ops):
    size = len(ops)
    if ops[size - 1].type != 'h':
        return

    opstr = gatherTypes(ops)

    # Rule 1: 
    # - H - H - => - I - => (None)
    if matchTypes(opstr, rules[0]) and \
        matchOperands(ops, [1, 2], [0, 0]):
        ops.pop()
        ops.pop()

    # Rule 2:
    # - H - S - H - => - S_dg - H - S_dg
    if matchTypes(opstr, rules[1]) and \
        matchOperands(ops, [1, 2, 3], [0, 0, 0]):
        ops[size - 1].change('sdg')
        ops[size - 2].change('h')
        ops[size - 3].change('sdg')
       
    # Rule 3:
    # - H - S_dg - H - => - S - H - S
    if matchTypes(opstr, rules[2]) and \
        matchOperands(ops, [1, 2, 3], [0, 0, 0]):
        ops[size - 1].change('s')
        ops[size - 2].change('h')
        ops[size - 3].change('s')
    
    # Rule 4:
    # - H - ■ - H -         - @ -
    #       |          =>     |
    # - H - @ - H -         - ■ -
    if matchTypes(opstr, rules[3]) and \
        ( (matchOperands(ops, [1, 4], [0, 0]) and matchOperands(ops, [2, 5], [0, 0])) or \
           (matchOperands(ops, [1, 5], [0, 0]) and matchOperands(ops, [2, 4], [0, 0])) ) and \
        ( (matchOperands(ops, [1, 3], [0, 0]) and matchOperands(ops, [2, 3], [0, 1])) or \
           (matchOperands(ops, [1, 3], [0, 1]) and matchOperands(ops, [2, 3], [0, 0])) ):
        operand = ops[size - 3].operands
        ops.pop(); ops.pop(); ops.pop(); ops.pop()
        op = ops.pop()
        op.change('cx', operand[::-1])
        ops.append(op)

    # Rule 5:
    # - - - - - ■ - - - - - -        - - - - ■ - - -
    #           |               =>           |
    # - H - S - @ - S_dg - H -      - S_dg - @ - S -
    if matchTypes(opstr, rules[4]) and \
        matchOperands(ops, [1, 2, 3, 4, 5], [0, 0, 1, 0, 0]):
        ops.remove(ops[size - 5])
        ops.pop()
        size -= 2
        ops[size - 1].change('s')
        ops[size - 3].change('sdg')
       
    # Rule 6:
    #  - - - - - - ■ - - - - -      - - - ■ - - -
    #              |            =>        |
    # - H - S_dg - @ - S - H -      - S - @ - S_dg -
    if matchTypes(opstr, rules[5]) and \
        matchOperands(ops, [1, 2, 3, 4, 5], [0, 0, 1, 0, 0]):
        ops.remove(ops[size - 5])
        ops.pop()
        size -= 2
        ops[size - 1].change('sdg')
        ops[size - 3].change('s')
        

HadamardReduction.min_size = 2
HadamardReduction.max_size = 5