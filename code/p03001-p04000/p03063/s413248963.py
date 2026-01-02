# coding:utf-8

import sys
# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


def main():
    n = II()
    s = SI()

    W = [0]
    B = [0]
    for c in s:
        b = c == '#'
        w = c == '.'
        B.append(B[-1] + b)
        W.append(W[-1] + w)

    res = n - max(B[-1], W[-1])
    for i in range(n - 1):
        res = min(res, B[i] + W[-1] - W[i + 1])

    return res


print(main())
