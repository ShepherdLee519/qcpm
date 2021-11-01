from collections import defaultdict


def generateCandidates(pos):
    pos = [ v for _,v in sorted(list(pos.items())) ]

    def recur(i):
        if i == len(pos):
            ans.append(temp[:])

            return

        for j in pos[i]:
            temp.append(j)
            recur(i + 1)
            temp.pop()

    ans = []
    temp = []
    recur(0)

    return ans

def numDistinct(s: str, t: str) -> int:
    if len(t) > len(s):
        return 0

    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    pos = defaultdict(list)

    for i in range(len(s) + 1):
        dp[i][0] = 1

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i-1] == t[j-1]:
                # print(f'pos ({i-1}, {j-1})')
                pos[j-1].append(i-1)
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    # return dp 
    # return dp[-1][-1]

    if dp[-1][-1] == 0:
        return []
    else:
        return generateCandidates(pos)


dp = numDistinct('abbccd', 'abcd')
print(dp)