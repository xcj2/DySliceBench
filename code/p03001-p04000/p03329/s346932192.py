import sys
sys.setrecursionlimit(1000000)


def power6(n, memo, s):
    memo[n] = min(memo[n], memo[n - s] + 1)
    if n - s * 6 < 0:
        return memo
    return power6(n, memo, s * 6)


def power9(n, memo, s):
    memo[n] = min(memo[n], memo[n - s] + 1)
    if n - s * 9 < 0:
        return memo
    return power9(n, memo, s * 9)


def search(n, memo, s):
    memo = power6(s, memo, 1)
    memo = power9(s, memo, 1)
    if s + 1 == n + 1:
        return memo
    return search(n, memo, s + 1)


n = int(input())
max_n = 110000
dp = [n] * max_n

# 初期化
dp[0] = 0
memo = search(n, dp, 0)
print(memo[n])
