from qcpm.operator import convert_type, Operator
from qcpm.reduction.common import solveRules, gatherTypes, matchTypes, matchOperands


rules = [
    # identity => ''
    ['id'],
    # single qubit reversible gates
    ['x', 'x'], ['y', 'y'], ['z', 'z'],
    # two qubits reversible gates
    ['cx', 'cx'],
]

rules = solveRules(rules)


def ReversibleReduction(ops):
    size = len(ops)

    # Case 1: identity cancellation
    if size == 1 and ops[0].type == 'id':
        ops.pop()
        return

    opstr = gatherTypes(ops)

    # Case 2: reversible single qubit gates
    single_qubit_gates = range(1, 4)
    for i in single_qubit_gates:
        if matchTypes(opstr, rules[i]) and \
            matchOperands(ops, [1, 2], [0, 0]):
        
            ops.pop()
            ops.pop()

    # Case 3: reversible two qubits gates
    two_qubits_gates = range(4, 5)
    for i in two_qubits_gates:
        if matchTypes(opstr, rules[i]) and \
            matchOperands(ops, [1, 2], [0, 0]) and \
            matchOperands(ops, [1, 2], [1, 1]):
        
            ops.pop()
            ops.pop()
        

ReversibleReduction.min_size = 1
ReversibleReduction.max_size = 2