import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
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
    n = I()
    a = LI()
    b = LI()

    def f(c,n):
        c0 = c[0]
        if len(c) == 1:
            return n % c0[0] + n // c0[0] * c0[1]

        r = n
        for i in range(0,n+1,c0[0]):
            t = i // c0[0] * c0[1] + f(c[1:], n-i)
            if r < t:
                r = t
        return r

    c = sorted([(ai,bi) for ai,bi in zip(a,b) if ai < bi], reverse=True)
    t = n
    if len(c) > 0:
        t = f(c,n)

    d = sorted([(ai,bi) for ai,bi in zip(b,a) if ai < bi], reverse=True)
    r = t
    if len(d) > 0:
        r = f(d,t)

    return r


print(main())

