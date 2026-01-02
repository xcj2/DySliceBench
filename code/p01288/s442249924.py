import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
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
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

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
    rr = []

    def f(n,q):
        ps = [0, 1] + [I() for _ in range(n-1)]
        qs = []
        ms = set()
        for i in range(q):
            s,t = LS()
            t = int(t)
            if s == 'M':
                if t in ms:
                    continue
                ms.add(t)
            qs.append((s,t))
        uf = UnionFind(n+1)
        for i in range(2,n+1):
            if i in ms:
                continue
            uf.union(i, ps[i])

        r = 0
        for s,t in qs[::-1]:
            if s == 'Q':
                r += uf.find(t)
            else:
                uf.union(t, ps[t])

        return r

    while 1:
        n,q = LI()
        if n == 0 and q == 0:
            break
        rr.append(f(n,q))

    return '\n'.join(map(str,rr))


print(main())

