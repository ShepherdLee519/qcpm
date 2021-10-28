from collections import deque

from qcpm.optimization.invoker import Reducer


_reductions = [
    Reducer('reversible'),
    Reducer('hadamard'),
]

def getMaxRuleSize(reductions):
    """
    :param reductions: [...] reduction runners
    :returns: max_rule_size
    """
    max_sizes = []

    for reduction in reductions:
        max_sizes.append( reduction.max_size )
    
    return max(max_sizes)

_rule_size_max = getMaxRuleSize(_reductions)


def reduction(operators):
    buffer = deque()

    for operator in operators:
        buffer.append(operator)

        # if rule_min_size = 2, rule_max_size = 5
        # -------------------------
        # Case 1. ['h'] => Nothing
        # Case 2. ['(h)hShsh'] => popleft()
        # Case 3. ['hsh'] => reduction(['hsh'])

        if len(buffer) > _rule_size_max:
            yield buffer.popleft()

        for reductionRule in _reductions:
            # remember that reduction will change buffer's size
            if len(buffer) >= reductionRule.min_size:
                reductionRule(buffer)
        
    while len(buffer) != 0:
        yield buffer.popleft()