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


def main():
    k = I()

    m = {}
    def f(i,t):
        k = (i,t)
        if k in m:
            return m[k]

        r = 0
        if i == 1:
            if t == -1:
                r = 9
            elif t == 0 or t == 9:
                r = 2
            else:
                r = 3
        else:
            if t == -1:
                r += f(i-1, -1)
                for nt in range(1, 10):
                    r += f(i-1, nt)
            else:
                for nt in range(max(0,t-1), min(10, t+2)):
                    r += f(i-1, nt)
        m[k] = r
        return r

    def g(i, t, k):
        if i == 1:
            if t == -1:
                return k
            if t == 0:
                return k - 1
            return t + k - 2

        if t == -1:
            f1 = f(i-1, -1)
            if f1 >= k:
                return g(i-1, -1, k)
            k -= f1
            for j in range(1, 10):
                fj = f(i-1, j)
                if fj >= k:
                    r = g(i-1, j, k)
                    return r + j * 10**(i-1)
                k -= fj
        else:
            for j in range(max(0, t-1), min(10, t+2)):
                fj = f(i-1, j)
                if fj >= k:
                    r = g(i-1, j, k)
                    return r + j * 10**(i-1)
                k -= fj

    r = g(11, -1, k)
    return r

print(main())



