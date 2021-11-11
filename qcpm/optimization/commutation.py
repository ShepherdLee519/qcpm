from collections import deque

from qcpm.optimization.invoker import Commutator


commutator = Commutator()

def commutation(operators):
    """ Commutation Generator.

    apply Commutation Pattern Mapping and yield the Operator after mapping.

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
        # Case 3. ['hsh'] => commutation(['hsh'])

        if len(buffer) > commutator.max_size:
            yield buffer.popleft()

        # remember that reduction will change buffer's size
        if len(buffer) >= commutator.min_size:
            commutator(buffer)
    
    # yield the left Operators
    while len(buffer) != 0:
        yield buffer.popleft()