# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1127

from decimal import Decimal, getcontext
from itertools import combinations
from heapq import *


getcontext().prec = 30

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
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

while True:
    N = int(input())
    if N ==0:
        exit()

    tree = UnionFind(N)

    pos = dict()
    for i in range(N):
        pos[i] = tuple(map(Decimal, input().split()))

    data = []

    for a,b in combinations(range(N), 2):
        x1,x2,x3,xr = pos[a]
        y1,y2,y3,yr = pos[b]
        cost = max(((x1-y1)**2 + (x2-y2)**2 + (x3-y3)**2).sqrt() -xr -yr, 0)
        data.append((a, b, cost))

    res = 0
    data.sort(key=lambda x: x[2])

    for a, b, cost in data:
        if tree.union(a,b):
            res += cost
    print("{:.03f}".format(res))
