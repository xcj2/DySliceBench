from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return S().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


class BIT:
    def __init__(self, size):
        self.bit = [0] * size
        self.size = size
        self.total = 0

    def add(self, i, w):
        x = i + 1
        self.total += w
        while x <= self.size:
            self.bit[x - 1] += w
            x += x & -x
        return

    def sum(self, i):
        res = 0
        x = i + 1
        while x:
            res += self.bit[x - 1]
            x -= x & -x
        return res

    def interval_sum(self, i, j): # i <= x < j の区間
        return self.sum(j - 1) - self.sum(i - 1) if i else self.sum(j - 1)


n = I()
s = list(S())
q = I()
D = defaultdict(lambda:BIT(n))
for j in range(n):
    D[s[j]].add(j, 1)

for _ in range(q):
    qi, i, c = LS()
    if qi == "1":
        i = int(i) - 1
        D[s[i]].add(i, -1)
        D[c].add(i, 1)
        s[i] = c
    else:
        l, r = int(i) - 1, int(c)
        ret = 0
        for k in range(97, 123):
            if D[chr(k)].interval_sum(l, r):
                ret += 1
        print(ret)




