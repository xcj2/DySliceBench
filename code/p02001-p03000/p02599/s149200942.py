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
INF = 10 ** 20
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


class BIT:
    def __init__(self, n):
        self.num = n
        self.dat = [0] * (self.num + 1)

    def add(self, i, x):
        i += 1
        while i <= self.num:
            self.dat[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.dat[i]
            i -= i & -i
        return s

n, q = LI()
ans = [0] * q
C = LI()
Q = [[] for _ in range(n)]
for i in range(q):
    l, r = LI()
    Q[r - 1] += [(i, l - 1)]

last = [-1] * (n + 1)
bit = BIT(n + 1)
for i, c in enumerate(C):
    col = C[i]
    bit.add(i, 1)
    if last[col] != -1:
        bit.add(last[col], -1)
    last[col] = i
    for qi, li in Q[i]:
        ans[qi] = bit.sum(i) - bit.sum(li - 1)


print(*ans, sep="\n")
