import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def inp():
    return int(input())
def inps():
    return input().rstrip()
def inpl():
    return list(map(int, input().split()))
def inpls():
    return list(map(str, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10

# from heapq import heappush, heappop, heapify
# import math
# from math import gcd
# import itertools as it
# import collections
# from collections import deque 

# ---------------------------------------
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
# ---------------------------

N, M = inpl()
graph = [[] for i in range(N + 1)]
uf = UnionFind(N + 1)

for i in range(M):
    a, b = inpl()
    uf.union(a, b)

print(len(uf.roots()) - 2)



