# coding:utf-8

import sys
import bisect

# from collections import Counter, defaultdict

INF = float('inf')
MOD = 10 ** 9 + 7


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()


N, M = LI()
A = LI()
B = LI()

A.sort()
B.sort()

SA = set(A)
SB = set(B)


if N != len(SA) or M != len(SB):
    print(0)
    exit()

ans = 1
num = 0
aa = N
bb = M
for i in range(1, N * M + 1)[::-1]:
    if i in SA and i in SB:
        pass
    elif i in SB:
        while aa != 0 and 0 < i <= A[aa - 1]:
            aa -= 1
        ans *= N - aa
        ans %= MOD
    elif i in SA:
        while bb != 0 and 0 < i <= B[bb - 1]:
            bb -= 1
        ans *= M - bb
        ans %= MOD
    else:
        while aa != 0 and 0 < i <= A[aa - 1]:
            aa -= 1
        while bb != 0 and 0 < i <= B[bb - 1]:
            bb -= 1
        ans *= (M - bb) * (N - aa) - num
        ans %= MOD
    num += 1
    # print(i, ans, num)

print(ans)
