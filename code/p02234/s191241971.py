import sys

sys.setrecursionlimit(10**7)

inf = float('inf')

def solve():
    n = int(sys.stdin.readline())

    r = [0] * n
    c = [0] * n

    for i in range(n):
        ri, ci = map(int, sys.stdin.readline().split())
        r[i] = ri
        c[i] = ci

    memo = [[-1]*(n + 1) for i in range(n + 1)]

    ans = mcm(memo, n, r, c, 0, n)

    # print(memo)

    print(ans)

def mcm(memo, n, r, c, left, right):
    if memo[left][right] != -1:
        return memo[left][right]
    elif right - left == 1:
        memo[left][right] = 0
        return 0
    else:
        res = inf

        for i in range(left + 1, right):
            res = min(res, mcm(memo, n, r, c, left, i) + mcm(memo, n, r, c, i, right) + r[left]*r[i]*c[right-1])

        memo[left][right] = res
        return res

def compute_lcs(x, y):
    n = len(x)
    m = len(y)

    x = '#' + x
    y = '#' + y

    dp = [[0]*(m + 1) for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

if __name__ == '__main__':
    solve()