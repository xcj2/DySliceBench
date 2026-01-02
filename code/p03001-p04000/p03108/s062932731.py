import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


class UnionFind():
    def __init__(self, n):
        self.par = [-1 for _ in range(n)]
        self.sizeDict = { i: 1 for i in range(n)}

    def unite(self, v1, v2):
        '''
        connect v2 to v1.

        parent: v1
        child: v2
        '''
        r1 = self.root(v1)
        r2 = self.root(v2)
        if r1 == r2:
            return
        self.par[r2] = r1
        self.sizeDict[r1] += self.sizeDict[r2]

    def root(self, v):
        if self.par[v] == -1:
            return v
        self.par[v] = self.root(self.par[v])
        return self.par[v]

    def sameRoot(self, v1, v2):
        return self.root(v1) == self.root(v2)

    def size(self, v):
        return self.sizeDict[self.root(v)]

def main():
    N, M = LI()
    edges = []
    for _ in range(M):
        a, b = LI_()
        edges.append((a, b))

    ans = [N*(N-1)//2]
    uf = UnionFind(N)
    for e in edges[::-1][:-1]:
        a, b = e[0], e[1]
        unconnected = uf.size(a) * uf.size(b)
        if uf.sameRoot(a, b):
            unconnected = 0
        ans.append(ans[-1] - unconnected)
        uf.unite(a, b)
    for a in ans[::-1]:
        print(a)
main()

