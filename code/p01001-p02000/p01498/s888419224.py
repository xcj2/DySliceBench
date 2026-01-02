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
    rr = []

    def f(n,w,h):
        wd = {}
        hd = {}
        kf = 0
        uf = UnionFind(n+1)
        uc = 0
        for i in range(n):
            x,y = LI()
            if x in wd:
                if uf.union(wd[x], i):
                    uc += 1
            else:
                wd[x] = i
            if y in hd:
                if uf.union(hd[y], i):
                    uc += 1
            else:
                hd[y] = i
            if x == 1 or y == 1 or x == w or y == h:
                kf = 1
        r = uc
        nk = n - uc
        if nk == 1:
            return r
        r += nk - kf + nk - 1

        return r

    while 1:
        n,w,h = LI()
        if n == 0:
            break
        rr.append(f(n,w,h))
        # print(n, rr[-1])
        break

    return '\n'.join(map(str, rr))


print(main())

