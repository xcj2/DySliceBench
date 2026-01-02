from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, cos, radians, pi, sin
from operator import mul
from functools import reduce
from operator import mul


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]


n = I()
P = LI()
L = [[min(x, y, n - x - 1, n - y - 1) for x in range(n)] for y in range(n)]
flg = [[1] * n for _ in range(n)]
ans = 0
for i in P:
    xi = (i - 1) % n
    yi = (i - 1) // n
    ans += L[yi][xi]
    flg[yi][xi] = 0
    q = [((i - 1) // n,  (i - 1) % n)]
    while q:
        a, b = q.pop()
        val = L[a][b] + flg[a][b]
        if a >= 1 and L[a - 1][b] > val:
            L[a - 1][b] = val
            q += [(a - 1, b)]
        if b >= 1 and L[a][b - 1] > val:
            L[a][b - 1] = val
            q += [(a, b - 1)]
        if a < n - 1 and L[a + 1][b] > val:
            L[a + 1][b] = val
            q += [(a + 1, b)]
        if b < n - 1 and L[a][b + 1] > val:
            L[a][b + 1] = val
            q += [(a, b + 1)]

print(ans)




