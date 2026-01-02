import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

class UnionFind:
    def __init__(self, size, tb):
        self.table = tb

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

    def subsetall(self):
        a = []
        for i in range(len(self.table)):
            if self.table[i] < 0:
                a.append((i, -self.table[i]))
        return a

def main():
    n,m = LI()
    x = LI()
    s = sum(x)
    t = []
    e = collections.defaultdict(list)
    for _ in range(m):
        a,b,y = LI()
        a -= 1
        b -= 1
        t.append((y,a,b))
        e[a].append((b,y))
        e[b].append((a,y))

    t = sorted(t)

    uf = UnionFind(n,[-c for c in x])
    ba = [None] * m
    for i in range(m):
        y,a,b = t[i]
        uf.union(a,b)
        k = -uf.table[uf.find(a)]
        if k >= y:
            ba[i] = 1


    uf2 = UnionFind(n,[-c for c in x])
    for i in range(m-1,-1,-1):
        if ba[i] is None:
            continue
        y,a,b = t[i]
        if not uf2.union(a,b):
            continue
        al = set([a,b])
        q = set([a,b])
        while q:
            nq = set()
            for o in q:
                for c,cy in e[o]:
                    if cy > y:
                        continue
                    if uf2.union(o,c):
                        nq.add(c)
            q = nq

    r = m
    for i in range(m):
        y,a,b = t[i]
        k = -uf2.table[uf2.find(a)]
        if k >= y:
            r -= 1

    return r



print(main())


