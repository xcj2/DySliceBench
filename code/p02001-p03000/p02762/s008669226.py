# Author: cr4zjh0bp
# Created: Fri Mar 13 19:30:22 UTC 2020
import sys
 
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
 
ni = lambda: int(ns())
nin = lambda y: [ni() for _ in range(y)]
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda y: [na() for _ in range(y)]
nf = lambda: float(ns())
nfn = lambda y: [nf() for _ in range(y)]
nfa = lambda: list(map(float, stdin.readline().split()))
nfan = lambda y: [nfa() for _ in range(y)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda y: [ns() for _ in range(y)]
ncl = lambda y: [list(ns()) for _ in range(y)]
nas = lambda: stdin.readline().split()

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self._size = [1 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self._size[y] += self._size[x]
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self._size[x] += self._size[y]
    
    def size(self, x):
        x = self.find(x)
        return self._size[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

n, m, k = na()
ab = nan(m)
cd = nan(k)

friend = defaultdict(int)
uf = UnionFind(n)

for i in range(m):
    a, b = ab[i]
    a -= 1
    b -= 1
    uf.unite(a, b)
    friend[a] += 1
    friend[b] += 1

block = defaultdict(list)
for i in range(k):
    c, d = cd[i]
    c -= 1
    d -= 1
    block[c].append(d)
    block[d].append(c)
ans = []
for i in range(n):
    bf = 0
    for j in block[i]:
        if uf.same(i, j):
            bf += 1
    ans.append(uf.size(i) - friend[i] - bf - 1)

print(*ans)