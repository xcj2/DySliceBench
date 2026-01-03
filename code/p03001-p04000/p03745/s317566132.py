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

    # 1: 単調非減少，2: 単調非増加，0: 未定
    state = 0
    prev = A[0]
    res = 1
    for cur in A:
        if state:
            if state == 1 and prev > cur:
                res += 1
                state = 0
            if state == 2 and prev < cur:
                res += 1
                state = 0
        else:
            if prev < cur:
                state = 1
            if prev > cur:
                state = 2
        prev = cur

    return res


print(main())
