from qcpm.common import timerDecorator


# @timerDecorator(description='genCandidates')
def _genCandidates(dp, i, j):
    ans = []
    temp = []

    def recur(posi, posj):
        if len(temp) == j:
            ans.append(temp[::-1])
            return
        if dp[posi][posj] == 0:
            return 
        # elif j - len(temp) > posj:
        #     return

        if dp[posi - 1][posj] == dp[posi][posj]:
            recur(posi - 1, posj)
        else:
            temp.append(posi - 1)
            recur(posi - 1, posj - 1)
            temp.pop()

            recur(posi - 1, posj)

    recur(i, j)

    return ans


# @timerDecorator(description='Positioning')
def positioning(circuit, pattern):
    """
    :params circuit: circuit.draft eg. chxcccx...
    :params pattern: eg. ccc
    """
    circuit_size, pattern_size = len(circuit), len(pattern)
    if pattern_size > circuit_size:
        return []
    
    dp = [[0] * (pattern_size + 1) for _ in range(circuit_size + 1)]

    for i in range(circuit_size + 1):
        dp[i][0] = 1

    for i in range(1, circuit_size + 1):
        for j in range(1, pattern_size + 1):
            if circuit[i-1] == pattern[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    if dp[-1][-1] == 0:
        return []
    else:
        return _genCandidates(dp, circuit_size, pattern_size)