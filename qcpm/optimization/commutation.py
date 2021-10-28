from collections import deque

from qcpm.optimization.invoker import Commutator

commutator = Commutator()

def commutation(operators):
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
        
    while len(buffer) != 0:
        yield buffer.popleft()