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
    s = SI()

    C = Counter(s)
    res = 1
    for c in C.values():
        res *= c + 1
        res %= MOD

    return res - 1 if res else MOD - 1


print(main())
