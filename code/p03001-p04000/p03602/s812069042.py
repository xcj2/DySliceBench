import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

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
    n = I()
    a = [LI() for _ in range(n)]
    for i in range(n):
        ai = a[i]
        for j in range(i+1,n):
            aij = ai[j]
            aj = a[j]
            for k in range(n):
                if ai[k] + aj[k] < aij:
                    return -1

    r = 0
    ij = sorted(list(itertools.chain.from_iterable([[[a[i][j], i, j] for j in range(i+1,n)] for i in range(n)])))
    uf = UnionFind(n)
    aa = [[inf] * n for _ in range(n)]
    for i in range(n):
        aa[i][i] = 0
    for k,i,j in ij:
        if uf.union(i,j):
            aa[i][j] = aa[j][i] = k
            r += k
        elif aa[i][j] > k:
            f = True
            for l in range(n):
                if f and aa[l][i] + aa[l][j] <= k:
                    aa[i][j] = aa[j][i] = aa[l][i] + aa[l][j]
                    f = False
                elif aa[l][i] + aa[l][j] < aa[i][j]:
                    aa[i][j] = aa[j][i] = aa[l][i] + aa[l][j]

            if f:
                aa[i][j] = aa[j][i] = k
                r += k

    for i in range(n):
        ai = a[i]
        aai = aa[i]
        for j in range(i+1,n):
            if ai[j] != aai[j]:
                return -1

    return r


print(main())



