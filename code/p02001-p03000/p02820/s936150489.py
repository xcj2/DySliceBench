import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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
    n,k = LI()
    r,s,p = LI()
    t = S()
    dp = [[0]*3 for _ in range(k)]
    for i in range(n):
        c = t[i]
        b = -1
        cp = dp[i%k]
        np = cp[:]
        mp = max(cp)
        if c == "r":
            np[2] = max(max(cp[0], cp[1]) + p, cp[2])
            np[1] = np[0] = mp
        elif c == "s":
            np[0] = max(max(cp[2], cp[1]) + r, cp[0])
            np[1] = np[2] = mp
        else:
            np[1] = max(max(cp[2], cp[0]) + s, cp[1])
            np[2] = np[0] = mp

        dp[i%k] = np

    return sum(map(max, dp))


print(main())


