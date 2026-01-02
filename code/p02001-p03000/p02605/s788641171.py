from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


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
mod = 10 ** 9 + 7


D_sum = defaultdict(list)
D_diff = defaultdict(list)
DX = defaultdict(list)
DY = defaultdict(list)
n = I()
L = []
ans = INF
for i in range(n):
    x, y, u = LS()
    x = int(x)
    y = int(y)
    D_sum[x + y] += [(x, u)]
    D_diff[x - y] += [(x, u)]
    if u in "UD":
        DX[x] += [(y, u)]
    else:
        DY[y] += [(x, u)]


for _, co_list in D_sum.items():
    co_list.sort()
    r = d = -INF
    for co, direction in co_list:
        if direction == "R":
            r = co
        elif direction == "D":
            d = co
        elif direction == "U":
            ans = min(co - r, ans)
        else:
            ans = min(co - d, ans)

for _, co_list in D_diff.items():
    co_list.sort()
    u = r = -INF
    for co, direction in co_list:
        if direction == "U":
            u = co
        elif direction == "R":
            r = co
        elif direction == "D":
            ans = min(co - r, ans)
        else:
            ans = min(co - u, ans)


for _, co_list in DX.items():
    co_list.sort()
    u = -INF
    for co, direction in co_list:
        coo = co
        if direction == "U":
            u = co
        else:
            ans = min((co - u) / 2, ans)


for _, co_list in DY.items():
    co_list.sort()
    r = -INF
    for co, direction in co_list:
        if direction == "R":
            r = co
        else:
            ans = min((co - r) / 2, ans)


if ans > 10 ** 8:
    print("SAFE")
else:
    print(int(ans * 10))







"""
L1 = []
L2 = []
L3 = []
L4 = []
for xk, yk ,u in L:
    L1 += [(xk - yk)]
    L2 += [(- xk - yk)]
    L3 += [(xk + yk)]
    L4 += [(- xk + yk)]

print(L1)
print(L2)
print(L3)
print(L4)

"""