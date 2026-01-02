def nCk(n, k):
    if k > n or min(n, k) < 0:
        return 0
    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i
    return res

def solveSmaller():
    return 9 ** k * nCk(n - 1, k)

def solveDp():
    global k
    dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]  # i, used k, smaller
    dp[0][1][0] = 1
    dp[0][1][1] = int(s[0]) - 1
    cnt = 1
    for i in range(1, n):
        cnt += s[i] != '0'
        for k in range(1, k + 1):
            dp[i][k][0] = cnt == k
            dp[i][k][1] = dp[i - 1][k][1] + \
                          (dp[i - 1][k][0] if s[i] != '0' else 0) + \
                          dp[i - 1][k - 1][1] * 9 + \
                          dp[i - 1][k - 1][0] * max(0, int(s[i]) - 1)
    return dp[n - 1][k][0] + dp[n - 1][k][1]

s = input()
k = int(input())
n = len(s)
print(solveSmaller() + solveDp())