from collections import defaultdict, deque, Counter
from heapq import heappush, heappop
from itertools import permutations, accumulate
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
# from fractions import gcd
# from math import gcd
import sys


def I(): return int(input())  # '123' -> 123


def Is(): return map(int, input().split())  # '123 456' -> 123, 456


def LI(): return list(map(int, input().split()))  # '123 456' -> [123, 456]


def TI(): return tuple(map(int, input().split()))  # '123 456' -> (123, 456)


def IR(n): return [I() for _ in range(n)]


def LIR(n): return [LI() for _ in range(n)]


def TIR(n): return [TI() for _ in range(n)]


def S(): return input()


def Ss(): return input().split()  # 'aa bb' -> 'aa','bb' or ['aa','bb']


def LS(): return list(input())  # 'abc123' -> ['a','b','c','1','2','3']


def SR(n): return [S() for _ in range(n)]


def SsR(n): return [Ss() for _ in range(n)]


def LSR(n): return [LS() for _ in range(n)]


sys.setrecursionlimit(1000000)
MOD = 1000000007
INF = float('inf')

N = I()
A = []
XY = []
for i in range(N):
    A.append(int(input()))
    XY.append([])
    for _ in range(A[i]):
        x, y = map(int, input().split())
        x -= 1
        XY[i].append((x, y))

ans = 0

for bit in range(1, 1 << N):
    contradiction = False
    for i in range(N):
        if bit & (1 << i):
            for x, y in XY[i]:
                if ((bit >> x) & 1) ^ y:
                    contradiction = True
    if not contradiction:
        ans = max(ans, bin(bit).count("1"))

print(ans)
