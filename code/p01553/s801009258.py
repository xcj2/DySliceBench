import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**3
eps = 1.0 / 10**10
mod = 10**9+7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    c = [S() for _ in range(n)]
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        ci = c[i]
        if ci == '-':
            for j in range(n+1):
                dp[i+1][j] = dp[i][j]
        elif ci == 'D':
            for j in range(n+1):
                dp[i+1][j] += dp[i][j] * j
                if j > 0:
                    dp[i+1][j-1] += dp[i][j] * j * j
                    dp[i+1][j-1] %= mod
        else: # 'U'
            for j in range(n+1):
                if j < n:
                    dp[i+1][j+1] += dp[i][j]
                dp[i+1][j] += dp[i][j] * j
                dp[i+1][j] %= mod

    return dp[-1][0] % mod


print(main())


