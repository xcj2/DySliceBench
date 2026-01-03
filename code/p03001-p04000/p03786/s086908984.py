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
    A.sort()

    C = [0]
    for a in A:
        C.append(C[-1] + a)

    t = 0
    for i, (a, c) in enumerate(zip(A[1:], C[1:-1])):
        # 1~kまでのサイズの和の2倍がk+1番目の生き物のサイズ未満なら1~kは最後まで生き残れない
        if a > 2 * c:
            t = i + 1

    return n - t


print(main())
