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


def M(n): return ModInt(n)

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

def main():
    n = I()
    xa = LI()

    m1 = M(1)
    c = [m1]
    for i in range(2, n+2):
        c.append(c[-1] + m1 / i)

    r = M(0)
    for i in range(1,n):
        t = xa[i] - xa[i-1]
        r += c[i-1] * t

    for i in range(n-1,1,-1):
        r *= i

    return r

print(main())



