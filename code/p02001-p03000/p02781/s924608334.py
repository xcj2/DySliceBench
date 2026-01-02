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
    n = I()
    k = I()
    a = [int(c) for c in str(n)]
    l = len(a)
    dp = [[[0]*(k+1) for j in range(2)] for i in range(l+1)]
    dp[0][0][0] = 1
    for i in range(l):
        cp = dp[i]
        np = dp[i+1]
        c = a[i]
        if c == 0:
            for j in range(2):
                for ck in range(k+1):
                    np[j][ck] += cp[j][ck]
        else:
            for j in range(2):
                for ck in range(k+1):
                    np[1][ck] += cp[j][ck]

        for v in range(1,10):
            if v == c:
                for ck in range(k):
                    np[0][ck+1] += cp[0][ck]
                    np[1][ck+1] += cp[1][ck]
            elif v < c:
                for ck in range(k):
                    np[1][ck+1] += cp[0][ck]
                    np[1][ck+1] += cp[1][ck]
            else:
                for ck in range(k):
                    np[1][ck+1] += cp[1][ck]

    r = dp[l][0][k] + dp[l][1][k]
    return r


print(main())



