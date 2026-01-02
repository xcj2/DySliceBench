# coding:utf-8

import sys
from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    C = [II() for _ in range(n)]

    dp = [0] * (n + 1)
    dp[0] = 1
    color_index = defaultdict(int)
    for i, c in enumerate(C):
        if not color_index[c]:
            color_index[c] = i + 1
            dp[i + 1] = dp[i]
        else:
            if color_index[c] == i:
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] = dp[i] + dp[color_index[c]]
                dp[i + 1] %= MOD
            color_index[c] = i + 1

    return dp[-1]


print(main())
