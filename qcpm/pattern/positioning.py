from qcpm.common import timerDecorator


def _add(elem, result):
    """
    Example:
        1. elem = 1, result = ""
            => "1"
        2. elem = 7, result = "1,4"
            => "1,4,7"
    """
    if len(result) == 0:
        return str(elem)
    else:
        return f"{result},{elem}"


def _apart(result, elem):
    """ test whether candidate pattern's gates are so far apart

    Args:
        result: string like "1,4"
        elem: int like 7, a position
    -------
    Returns:
        True => so far apart => not a proper candidate, else True
    -------
    Example:
        result: "1,4", elem = 51 (when distance_limit = 50)
            => False
    """
    distance_limit = 50

    if result == '':
        return False

    # result = "1,4,7" => begin = 1
    begin = int(result.split(',')[0])

    # for result = "1,4,7", elem = 52
    # just test the distance between the begining of result and elem.
    return elem - begin > distance_limit


# @timerDecorator(description='Positioning')
def positioning(circuit_str, pattern_str):
    """ find the mapped pattern position

    Args:
        circuit_str: circuit.draft eg. chxcccx...
        pattern_str: eg. ccc
    """
    circuit_size, pattern_size = len(circuit_str), len(pattern_str)

    # Can't match
    if pattern_size > circuit_size:
        return []
    
    dp = [0] * (pattern_size + 1)
    dp[0] = 1
    res = [ [''] for i in range(pattern_size + 1) ]

    for i in range(1, circuit_size + 1):
        # pattern_size down to 1
        for j in range( min(i, pattern_size), 0, -1 ):
            if circuit_str[i - 1] == pattern_str[j - 1]:
                dp[j] = dp[j] + dp[j - 1]

                for result in res[j - 1]:
                    if _apart(result, i - 1):
                        continue
                    # eg. result = "1,4", i - 1 = 7
                    # after _add => "1,4,7"
                    # res[j].append("1,4,7")
                    # 
                    res[j].append( _add(i - 1, result) )

    # res[pattern_size] contains final results like:
    # ["1,4,7", "1,5", "2,3,8", ...]
    #
    # 1. map(lambda a: a.split(','), ...)
    #   => [['1', '4', '7'], ['1', '5'], ['2', '3', '8'], ...]
    # 
    # 2. filter(lambda r: len(r) == pattern_size, ...)
    #   => [['1', '4', '7'], ['2', '3', '8'], ...]
    # 
    # 3. map(lambda arr: [int(a) for a in arr], ...)    
    #   => [[1, 4, 7], [2, 3, 8], ...]
    # 
    return map(
        lambda arr: [int(a) for a in arr], 
        filter(
            lambda r: len(r) == pattern_size, 
            map(lambda a: a.split(','), res[pattern_size])
        )
    )
    