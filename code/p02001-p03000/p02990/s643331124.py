import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

fac = [-1] * (10**7+1)
finv = [-1] * (10**7+1)
inv = [-1] * (10**7+1)

fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

def initNCMMod(limit):
    for i in range(2, limit):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod

def NCMMod(n, k):
    if n < k:
        return 0
    if (n < 0 or k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

dp = [[0 for _ in range(2001)] for __ in range(2001)]

def initSplitNintoKMod():
    for j in range(2001):
        dp[0][j] = 1

    for i in range(1, 2001):
        for j in range(1, 2001):
            if i - j >= 0:
                a = dp[i-j][j]
            else:
                a = 0
            dp[i][j] = dp[i][j-1] + a
            dp[i][j] %= mod

def splitNintoKMod(n, k):
    # at least 1 ball for each k boxes
    if n < k:
        return 0
    n = n - k
    if n <= 0 or k <= 0:
        return 0
    return dp[n][k]

initNCMMod(4000)

def main():
    N, K = LI()
    for i in range(1, K+1):
        ans = NCMMod(N-K+1, i) * NCMMod(K-1, i-1) % mod
        print(ans)

main()

