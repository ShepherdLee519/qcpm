from collections import deque

from qcpm.reduction.hadamard import HadamardReduction
from qcpm.reduction.common import getRuleSize


_reductions = [
    HadamardReduction,
]

_rule_size_min, _rule_size_max = getRuleSize(_reductions)


def reduction(operators):
    buffer = deque()

    for operator in operators:
        buffer.append(operator)

        if len(buffer) > _rule_size_max:
            yield buffer.popleft()

        if len(buffer) >= _rule_size_min:
            for reductionRule in _reductions:
                reductionRule(buffer)

    while len(buffer) != 0:
        yield buffer.popleft()