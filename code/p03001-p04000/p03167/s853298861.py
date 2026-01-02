# coding:utf-8

import sys

INF = 10 ** 5
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


h, w = LI()
B = [SI() for _ in range(h)]

dp = [[0] * (w + 1) for _ in range(h + 1)]
dp[0][1] = 1

for i in range(h):
    for j in range(w):
        if B[i][j] == '#':
            continue
        dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j]) % MOD

print(dp[-1][-1])
