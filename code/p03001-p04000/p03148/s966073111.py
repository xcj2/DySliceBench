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


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n, k = LI()
L = []
for kind, point in LIR(n):
    L += [(point, kind)]


L.sort()
que1 = deque(L[-k:])
que2 = deque(L[:-k])
ret = sum([point for point, kind in que1])
kind_cnt = Counter([i[1] for i in que1])
now_kinds = len(kind_cnt)
ans = ret + now_kinds ** 2
while que1:
    point1, kind1 = que1.popleft()
    if kind_cnt[kind1] > 1:
        kind_cnt[kind1] -= 1
        ret -= point1
        while que2:
            point2, kind2 = que2.pop()
            if not kind_cnt[kind2]:
                kind_cnt[kind2] += 1
                ret += point2
                now_kinds += 1
                ans = max(ans, ret + now_kinds ** 2)
                break
        else:
            break



print(ans)