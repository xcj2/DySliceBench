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
    n, m, c = LI()
    B = LI()

    res = 0
    for _ in range(n):
        A = LI()
        tmp = c
        for i in range(m):
            tmp += A[i] * B[i]
        if tmp > 0:
            res += 1

    return res


print(main())
