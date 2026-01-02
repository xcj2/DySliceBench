import sys
sys.setrecursionlimit(10000000)
def input():
    return sys.stdin.readline()[:-1]
from bisect import *
from collections import *
from heapq import *
import itertools
INF = 10**10
MOD = 10**9+7

class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.height = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def getsize(self, x):
        return self.size[self.find(x)]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.height[x] < self.height[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = self.par[x]
            self.size[x] += self.size[y]
            if self.height[x] == self.height[x]:
                self.height[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

def slide_min(a, k):
    n = len(a)
    b = [None] * (n-k+1)
    deq = deque()
    for i in range(n):
        while len(deq) > 0 and a[i] <= a[deq[-1]]:
            deq.pop()
        deq.append(i)
        if i-k+1 >= 0:
            b[i-k+1] = a[deq[0]]
            if deq[0] == i-k+1:
                deq.popleft()
    return b

def slide_max(a, k):
    n = len(a)
    b = [None] * (n-k+1)
    deq = deque()
    for i in range(n):
        while len(deq) > 0 and a[i] >= a[deq[-1]]:
            deq.pop()
        deq.append(i)
        if i-k+1 >= 0:
            b[i-k+1] = a[deq[0]]
            if deq[0] == i-k+1:
                deq.popleft()
    return b

N, K = map(int, input().split())
P = [int(x) for x in input().split()]
uf1 = UnionFind(N)
for i in range(N-1):
    if P[i] < P[i+1]:
        uf1.unite(i, i+1)
vs = []
for i in range(N-K+1):
    if uf1.same(i, i+K-1):
        vs.append(i)
uf2 = UnionFind(N)
if len(vs) > 1:
    for v1, v2 in zip(vs, vs[1:]):
        uf2.unite(v1, v2)
m, M = slide_min(P, K), slide_max(P, K)
for i in range(N-K):
    if P[i] == m[i] and P[i+K] == M[i+1]:
        uf2.unite(i, i+1)
s = set()
for i in range(N-K+1):
    s.add(uf2.find(i))
print(len(s))
