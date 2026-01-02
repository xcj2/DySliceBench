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
    x,y,a,b,c = LI()
    p = sorted(LI()) + [inf]
    q = sorted(LI()) + [inf]
    r = [-1] + sorted(LI())
    pi = a - x
    qi = b - y
    ri = c
    while True:
        if p[pi] < q[qi]:
            if p[pi] >= r[ri]:
                break
            pi += 1
            ri -= 1
        else:
            if q[qi] >= r[ri]:
                break
            qi += 1
            ri -= 1

    return sum(p[pi:-1] + q[qi:-1] + r[ri+1:])

print(main())



