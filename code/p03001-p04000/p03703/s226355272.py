import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

class Seg():
    def __init__(self, n, default, func):
        i = 1
        while 2**i <= n:
            i += 1
        self.D = default
        self.H = i
        self.N = 2**i
        self.A = [default] * (self.N*2-1)
        self.F = func

    def find(self, i):
        return self.A[i + self.N - 1]

    def update(self, i, x):
        i += self.N - 1
        self.A[i] = x
        while i > 0:
            i = (i-1) // 2
            self.A[i] = self.merge(self.A[i*2+1], self.A[i*2+2])

    def merge(self, a, b):
        return self.F(a, b)

    def total(self):
        return self.A[0]

    def query(self, a, b):
        def _query(k,l,r):
            if r <= a or b <= l:
                return self.D
            if a <= l and r <= b:
                return self.A[k]
            m = (l+r)//2
            vl = _query(k*2+1,l,m)
            vr = _query(k*2+2,m,r)
            return self.merge(vl,vr)
        return _query(0,0,self.N)

def main():
    n,k = LI()
    a = [I() for _ in range(n)]

    b = [0]
    for i in range(n):
        b.append(b[-1] + a[i] - k)

    d = {}
    for c,i in zip(sorted(set(b)), range(n+1)):
        d[c] = i
    e = [d[c] for c in b]

    l = len(d)

    def f(a,b):
        return a+b

    seg = Seg(l, 0, f)
    for c in e:
        seg.update(c, seg.find(c) + 1)

    r = 0
    for c in e[::-1]:
        t = seg.query(0,c+1)
        r += t-1
        seg.update(c, seg.find(c) - 1)

    return r

print(main())

