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
    A = LI()

    B = [0]
    for a in A:
        B.append(B[-1] + a)
    C = Counter(B)

    res = 0
    for c in C.values():
        res += c * (c - 1) // 2

    return res


print(main())
