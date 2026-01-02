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
    n,m = LI()
    sc = [LI() for _ in range(m)]
    t = [-1] * n
    for s,c in sc:
        s -= 1
        if t[s] >= 0:
            if t[s] != c:
                return -1
        else:
            t[s] = c
    if n == 1:
        if t[0] == -1:
            t[0] = 0
    else:
        if t[0] == 0:
            return -1
        if t[0] == -1:
            t[0] = 1
        for i in range(1,n):
            if t[i] < 0:
                t[i] = 0

    return JA(t, "")


print(main())



