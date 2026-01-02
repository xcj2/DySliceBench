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
    A = LI()

    minus = 0
    for a in A:
        if a < 0:
            minus += 1

    abs_A = [abs(a) for a in A]
    if minus % 2:
        return sum(abs_A) - min(abs_A) * 2
    else:
        return sum(abs_A)


print(main())
