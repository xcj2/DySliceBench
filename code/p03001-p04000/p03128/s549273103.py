# coding:utf-8

import sys
import math
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
    A.sort()
    A.reverse()

    match = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    # dp[i]: ちょうどマッチをi本使ったときに作れる整数の最大の桁数（-1: 作れない）
    dp = [-1] * (n + 1)
    dp[0] = 0
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in A:
            # 最上位桁の数字を決める
            # k: 最上位桁をjにしたときの残りのマッチの数
            k = i - match[j - 1]
            if k < 0 or dp[k] == -1:
                continue

            if dp[i] < dp[k] + 1:
                dp[i] = dp[k] + 1
                res[i] = max(j * 10 ** dp[k] + res[k], res[k] * 10 + j)

    return res[n]


print(main())
