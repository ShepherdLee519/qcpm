from collections import deque

from qcpm.optimization.invoker import Reducer


_reductions = [
    Reducer('reversible'),
    Reducer('hadamard'),
]

##########################
#                        #
#     Tool Functions     #
#                        #
##########################

def getMaxRuleSize(reductions):
    """
    Args:
        reductions: [...] reduction runners
    -------
    Returns: 
        max_rule_size
    """
    max_sizes = []

    for reduction in reductions:
        max_sizes.append( reduction.max_size )
    
    return max(max_sizes)

_rule_size_max = getMaxRuleSize(_reductions)

###############################
#                             #
#     Reduction Generator     #
#                             #
###############################

def reduction(operators):
    """ Reduction Generator.

    apply Reduction Pattern Mapping and yield the Operator after mapping.

    Args:
        operators: list of Operator / 
            or a generator which generates Operator thus can compose to be a pipe.
    """
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
        
    # yield the left Operators
    while len(buffer) != 0:
        yield buffer.popleft()