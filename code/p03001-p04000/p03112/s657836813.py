# coding:utf-8

import sys
import bisect
# from collections import Counter, defaultdict

INF = float('inf')
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
    ans = INF
    x_a = bisect.bisect_left(A, x)
    for k in [-1, 0]:
        tmp = abs(x - A[x_a + k])
        x_b = bisect.bisect_left(B, A[x_a + k])
        tmp += min(abs(B[x_b] - A[x_a + k]), abs(B[x_b - 1] - A[x_a + k]))
        ans = min(ans, tmp)

    x_b = bisect.bisect_left(B, x)
    for k in [-1, 0]:
        tmp = abs(x - B[x_b + k])
        x_a = bisect.bisect_left(A, B[x_b + k])
        tmp += min(abs(A[x_a] - B[x_b + k]), abs(A[x_a - 1] - B[x_b + k]))
        ans = min(ans, tmp)

    print(ans)
