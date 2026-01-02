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
        self.parent = [i for i in range(n)]

    def unite(self, a, b):
        # set a's parent as b's parent
        r1 = self.root(a)
        r2 = self.root(b)
        if r1 == r2:
            return
        self.parent[r2] = r1

    def root(self, a):
        if self.parent[a] == a:
            return a
        par = self.root(self.parent[a])
        self.parent[a] = par
        return par

    def sameRoot(self, a, b):
        return self.root(a) == self.root(b)

    def reroot(self):
        for ix, a in enumerate(self.parent):
            self.parent[ix] = self.root(a)
        return

def main():
    N, M = LI()
    P = LI_()
    X, Y = [], []
    uf = UnionFind(N)
    for _ in range(M):
        x, y = LI_()
        uf.unite(x, y)
    cnt = 0
    for ix, p in enumerate(P):
        if uf.sameRoot(ix, P[ix]):
            cnt += 1
    print(cnt)
main()

