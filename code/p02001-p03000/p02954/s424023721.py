from collections import Counter
from collections import deque
from functools import reduce
from operator import mul
from pprint import pprint
import bisect
import copy
import fractions
import itertools
import math
import queue
import random
import sys
import time
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def MI(): return map(int, sys.stdin.readline().split())
def II(): return int(sys.stdin.readline())
def IS(): return input()
def C(x): return Counter(x)
def GCD_LIST(numbers): return reduce(fractions.gcd, numbers)
def LCM_LIST(numbers): return reduce(LCM, numbers)
def LCM(m, n): return (m * n // fractions.gcd(m, n))
def COMBINATION(n, r):
    if n < 0 or r < 0 or n < r:
        return 0
    r = min(n-r, r)
    if r == 0:
        return 1
    o = reduce(mul, range(n, n - r, -1))
    u = reduce(mul, range(1, r + 1))
    return o // u
class UnionFind():

    def __init__(self, n):
        self.n = n
        self.node = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def same(self, x, y):
        return bool(self.root(x) == self.root(y))

    def root(self, x):
        if self.node[x] == x:
            return x
        else:
            self.node[x] = self.root(self.node[x])  # 経路圧縮
            return self.node[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return  # 結合不要
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.node[y] = x
        self.size[x] += self.size[y]

    def return_size(self, x):
        return self.size[self.root(x)]


s = IS()
right = [0] * len(s)
left = [0] * len(s)
for i in range(len(s)-1):
    if s[i] == 'R':
        if s[i+1] == 'L':
            right[i] += 1
        else:
            right[i+2] += 1
            right[i+2] += right[i]
            right[i] = 0

# print(right)

for i in range(len(s)-1, 0, -1):
    if s[i] == 'L':
        if s[i-1] == 'R':
            left[i] += 1
        else:
            left[i-2] += 1
            left[i-2] += left[i]
            left[i] = 0


# print(left)

ans = [right[i] + left[i] for i in range(len(s))]
print(*ans)
