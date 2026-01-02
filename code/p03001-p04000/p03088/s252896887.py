# coding:utf-8

import sys
import itertools

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()

    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
    # 初期状態は直近3文字がTTTと見なせる
    dp[0][3][3][3] = 1

    A, C, G, T = 0, 1, 2, 3
    for i in range(n):
        for a, b, c, d in itertools.product(range(4), repeat=4):
            if b == A and c == G and d == C: continue
            if b == A and c == C and d == G: continue
            if b == G and c == A and d == C: continue
            if a == A and b == G and d == C: continue
            if a == A and c == G and d == C: continue
            dp[i + 1][b][c][d] = (dp[i + 1][b][c][d] + dp[i][a][b][c]) % MOD

    ans = 0
    for a, b, c in itertools.product(range(4), repeat=3):
        ans = (ans + dp[n][a][b][c]) % MOD

    return ans


print(main())
