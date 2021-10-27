from qcpm.operator.convert import convert_type


def getMaxRuleSize(reductions):
    """
    :param reductions: [...] reduction runners
    :returns: max_rule_size
    """
    max_sizes = []

    for reduction in reductions:
        max_sizes.append( reduction.max_size )
    
    return max(max_sizes)

def solveRules(rules):
    """
    :param rules: [...] reduction rules
        eg. rules = 
        [
            ['h', 'h'],
            ['h', 'sdg', 'h'],
            ...
        ]
    :returns: 
        [
            'hh', 'hSh', ...
        ]
    """
    return [
        ''.join(map(lambda k:convert_type(k), rule)) for rule in rules
    ]

def gatherTypes(ops):
    """
    :param ops: [Operator('h'), Operator('cx'),...] Operators
    :returns: 'hc...'
    """
    return ''.join(convert_type(op.type) for op in ops)

def matchTypes(opstr, pattern):
    """
    :param opstr: 'cchsh'
    :param pattern: 'hsh'
    :returns: match True, else False
    """
    size = len(pattern)
    if len(opstr) < size:
        return False
    else:
        return opstr[-size:] == pattern

def matchOperands(ops, index, positions):
    """
            - - ■ - - 
                |      
            H - @ - H
        ----------------
        => matchOperands(ops, [1, 2, 3], [0, 1, 0])
    """
    size = len(ops)
    operand = ops[size - index[0]].operands[positions[0]]
    flag = True

    for i in range(1, len(index)):
        if ops[size - index[i]].operands[positions[i]] != operand:
            flag = False
            break
    
    return flag