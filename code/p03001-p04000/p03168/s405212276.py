# coding:utf-8

import sys
import numpy as np

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    P = LF()

    dp = np.zeros(n + 1, dtype=float)
    dp[0] = 1

    for p in P:
        tmp = dp * (1 - p)
        tmp[1:] += dp[:-1] * p
        dp = tmp

    return np.sum(dp[n // 2 + 1:])


print(main())
