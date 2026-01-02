# coding:utf-8

import sys
INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n, m = LI()
    A = LI()

    match = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    # dp[i]: ちょうどマッチをi本使ったときに作れる整数の最大の値
    dp = [-INF] * (n + 10)
    dp[0] = 0
    for i in range(n):
        for a in A:
            j = i + match[a]
            dp[j] = max(dp[j], dp[i] * 10 + a)

    return dp[n]


print(main())
