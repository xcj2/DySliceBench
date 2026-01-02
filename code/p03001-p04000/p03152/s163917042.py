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
    h, w = LI()
    A = LI()
    A.sort()
    B = LI()
    B.sort()

    # A, B内では同じ値は存在できない
    if len(A) != len(set(A)) or len(B) != len(set(B)):
        return 0

    a_i, b_i = h - 1, w - 1
    if h * w > A[a_i] or h * w > B[b_i]:
        return 0

    res = 1
    for n in range(1, h * w + 1)[::-1]:
        while a_i > 0 and A[a_i - 1] >= n:
            a_i -= 1
        while b_i > 0 and B[b_i - 1] >= n:
            b_i -= 1

        if n == A[a_i] and n == B[b_i]:
            res *= 1
        elif n == A[a_i]:
            res *= w - b_i
        elif n == B[b_i]:
            res *= h - a_i
        else:
            res *= (h - a_i) * (w - b_i) - (h * w - n)

        res %= MOD

    return res


print(main())
