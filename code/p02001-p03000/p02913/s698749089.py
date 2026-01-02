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

class ModInt():
    def __init__(self, n):
        self.n = n

    def __add__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n+x) % mod)

    def __sub__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n-x) % mod)

    def __mul__(self, x):
        x = ModInt.xn(x)
        return ModInt((self.n*x) % mod)

    def __truediv__(self, x):
        x = ModInt.xn(x)
        return ModInt(self.n * pow(x, mod-2, mod) % mod)

    @classmethod
    def xn(cls, x):
        if isinstance(x, ModInt):
            return x.n
        return x

    def __str__(self):
        return str(self.n)

def M(n): return ModInt(n)

class RollingHash():
    def __init__(self, s):
        self.N = n = len(s)
        a = [ord(c) for c in s]
        self.A1 = a1 = [M(a[0])]
        self.A2 = a2 = [M(a[0])]
        for c in a[1:]:
            a1.append(a1[-1] * 997 + c)
            a2.append(a2[-1] * 991 + c)

    def get(self, l, r):
        if l == 0:
            return (self.A1[r].n, self.A2[r].n)
        t1 = (self.A1[r] - self.A1[l-1] * pow(997, r-l+1, mod)).n
        t2 = (self.A2[r] - self.A2[l-1] * pow(991, r-l+1, mod)).n
        return (t1, t2)

def bs(f, mi, ma):
    mm = -1
    while ma > mi:
        mm = (ma+mi) // 2
        if f(mm):
            mi = mm + 1
        else:
            ma = mm
    if f(mm):
        return mm + 1
    return mm

def main():
    n = I()
    s = S()
    rh = RollingHash(s)

    def f(i):
        s = set()
        for j in range(i,n-i+1):
            t = rh.get(j-i,j-1)
            s.add(t)
            k = rh.get(j,j+i-1)
            if k in s:
                return True
        return False

    r = bs(f,1, n)

    return r - 1


print(main())



