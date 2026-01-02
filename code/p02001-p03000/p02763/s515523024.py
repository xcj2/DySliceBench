import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


class Seg():
    def __init__(self, na, default, func):
        if isinstance(na, list):
            n = len(na)
        else:
            n = na
        i = 1
        while 2**i <= n:
            i += 1
        self.D = default
        self.H = i
        self.N = 2**i
        if isinstance(na, list):
            self.A = [default] * (self.N) + na + [default] * (self.N-n)
            for i in range(self.N-1,0,-1):
                self.A[i] = func(self.A[i*2], self.A[i*2+1])
        else:
            self.A = [default] * (self.N*2)
        self.F = func

    def find(self, i):
        return self.A[i + self.N]

    def update(self, i, x):
        i += self.N
        self.A[i] = x
        while i > 1:
            i = i // 2
            self.A[i] = self.merge(self.A[i*2], self.A[i*2+1])

    def merge(self, a, b):
        return self.F(a, b)

    def total(self):
        return self.A[1]

    def query(self, a, b):
        A = self.A
        l = a + self.N
        r = b + self.N
        res = self.D
        while l < r:
            if l % 2 == 1:
                res = self.merge(res, A[l])
                l += 1
            if r % 2 == 1:
                r -= 1
                res = self.merge(res, A[r])
            l >>= 1
            r >>= 1

        return res

def main():
    n = I()
    s = S()
    q = I()
    qa = [LS() for _ in range(q)]
    aa = [[0]*26]
    oa = ord('a')
    for c in s:
        t = [0] * 26
        t[ord(c) - oa] = 1
        aa.append(t)

    def f(a,b):
        return [a[i]+b[i] for i in range(26)]

    seg = Seg(aa,[0]*26,f)
    r = []
    for t,a,b in qa:
        if t == '1':
            u = [0] * 26
            u[ord(b) - oa] = 1
            seg.update(int(a),u)
        else:
            c = seg.query(0,int(a))
            d = seg.query(0,int(b)+1)
            r.append(len([1 for i in range(26) if c[i] != d[i]]))

    return JA(r, '\n')


print(main())



