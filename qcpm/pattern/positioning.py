import copy

from qcpm.common import timerDecorator


def _add(elem, str_):
    if len(str_) == 0:
        return str(elem)
    else:
        return f"{str_},{elem}"

def _union(arr_a, str_b):
    arr_a.append(str_b)

    return arr_a


@timerDecorator(description='Positioning')
def positioning(circuit, pattern):
    """
    :params circuit: circuit.draft eg. chxcccx...
    :params pattern: eg. ccc
    """
    circuit_size, pattern_size = len(circuit), len(pattern)
    if pattern_size > circuit_size:
        return []
    
    dp = [0] * (pattern_size + 1)
    dp[0] = 1
    res = [[''] for i in range(pattern_size + 1)]

    for i in range(1, circuit_size + 1):
        for j in range( min(i, pattern_size), 0, -1 ):
            if circuit[i - 1] == pattern[j - 1]:
                dp[j] = dp[j] + dp[j - 1]
                for r in res[j - 1]:
                    res[j] = _union(res[j], _add(i - 1, r))

    return list(
        map(
            lambda arr: [int(a) for a in arr], 
            filter(
                lambda r: len(r) == pattern_size, 
                map(lambda a: a.split(','), res[pattern_size])
            )
        )
    )