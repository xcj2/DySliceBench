# coding:utf-8

import sys
from bisect import bisect_left

INF = 10 ** 18
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


a, b, q = LI()
A = [-INF] + [II() for _ in range(a)] + [INF]
B = [-INF] + [II() for _ in range(b)] + [INF]

for _ in range(q):
    x = II()
    s = bisect_left(A, x)
    t = bisect_left(B, x)

    res = INF
    for aa in [A[s - 1], A[s]]:
        for bb in [B[t - 1], B[t]]:
            d1 = abs(x - aa) + abs(aa - bb)
            d2 = abs(x - bb) + abs(bb - aa)
            res = min(res, d1, d2)

    print(res)
