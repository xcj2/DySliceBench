# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


n = I()

dp = [[0] * (n + 1) for _ in range(3)]
for i in range(n):
    H = LI()
    for k in range(3):
        k1, k2 = (k + 1) % 3, (k + 2) % 3
        dp[k1][i + 1] = max(dp[k1][i + 1], dp[k][i] + H[k1])
        dp[k2][i + 1] = max(dp[k2][i + 1], dp[k][i] + H[k2])

print(max([dp[k][n] for k in range(3)]))
