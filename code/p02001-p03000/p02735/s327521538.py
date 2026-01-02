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
    h,w = LI()
    aa = [[0 if c == '.' else 1 for c in S()] for _ in range(h)]

    dp = [[[inf]*2 for _ in range(w)] for __ in range(h)]
    dp[0][0][aa[0][0]] = aa[0][0]
    for i in range(h):
        for j in range(w):
            k = aa[i][j]
            if i > 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][1-k]+1)
            if j > 0:
                dp[i][j][k] = min(dp[i][j][k], dp[i][j-1][k])
                dp[i][j][k] = min(dp[i][j][k], dp[i][j-1][1-k]+1)

    return min(dp[-1][-1][0] + 1, dp[-1][-1][1] + 2) // 2


print(main())



