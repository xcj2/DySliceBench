import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


A, B, C, D = na()

mod = 998244353

dp = [[0] * (D + 1) for _ in range(C + 1)]

dp[A][B] = 1
for a in range(A + 1, C + 1):
    dp[a][B] = (dp[a - 1][B] * B) % mod

for b in range(B + 1, D + 1):
    dp[A][b] = (dp[A][b - 1] * A) % mod

for a in range(A + 1, C + 1):
    for b in range(B + 1, D + 1):
        dp[a][b] = (dp[a - 1][b] * b + dp[a][b - 1] * a -
                    dp[a - 1][b - 1] * (a - 1) * (b - 1)) % mod

print(dp[C][D])
