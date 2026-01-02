# coding:utf-8

import sys

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


N, W = LI()
L = [LI() for _ in range(N)]
V = 0
for i in range(N): V += L[i][1]

# dp[v]: 価値vを詰め込んだナップザックの重量の最小値
dp = [INF] * (V + 1)
dp[0] = 0
for weight, value in L:
    for v in range(V + 1)[::-1]:
        if v - value < 0:
            continue
        dp[v] = min(dp[v], dp[v - value] + weight)

for i in range(V + 1)[::-1]:
    if dp[i] != INF and dp[i] <= W:
        print(i)
        exit()
