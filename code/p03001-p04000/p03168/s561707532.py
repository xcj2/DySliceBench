# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n = II()
P = LF()

# dp[i][j]: i番目のコインまで投げた時，j枚のコインが表になる確率
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

# 調和級数
# O(NlogN)
for i in range(n):
    for j in range(i + 1):
        if dp[i][j] == 0:
            continue
        # P[i]が裏
        dp[i + 1][j] += dp[i][j] * (1 - P[i])
        # P[i]が表
        dp[i + 1][j + 1] += dp[i][j] * P[i]

print(sum(dp[n][n // 2 + 1:]))
