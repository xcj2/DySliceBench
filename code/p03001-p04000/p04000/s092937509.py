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
import pprint
sys.setrecursionlimit(10 ** 9)


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
mod = 1000000007



h, w, n = LI()
D = defaultdict(int)
for _ in range(n):
    a, b = LI()
    a -= 1; b -= 1;
    for i, j in product(range(a - 1, a + 2), range(b - 1, b + 2)):
        if 1 <= i < h - 1 and 1 <= j < w - 1:
            D[(i, j)] += 1


ans = [0] * 10
for k, v in D.items():
    ans[v] += 1



ans[0] = (h - 2) * (w - 2) - sum(ans)
print('\n'.join(list(map(str, ans))))