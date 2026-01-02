from collections import Counter,defaultdict,deque
from heapq import heapify,heappop,heappush
import sys,bisect,math,itertools,string,queue
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    #根を返す
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

n,m = inpl()
p = inpl()
uf = UnionFind(n)
for i in range(m):
    a,b = inpl()
    uf.union(a-1,b-1)
res = 0
for i in range(n):
    if uf.find(p[i]-1) == uf.find(i):
        res += 1
print(res)    
