import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 998244353

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, S = LI()
    a = LI()
    dp = [[0 for _ in range(S+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = dp[i-1][0] * 2 + 1
        dp[i][0] %= mod
    for i in range(N):
        for j in range(1, S+1):
            if j - a[i] >= 0:
                dp[i+1][j] = (dp[i][j-a[i]] % mod) + (dp[i][j] * 2 % mod)
            else:
                dp[i+1][j] = dp[i][j] * 2 % mod
            if j == a[i]:
                dp[i+1][j] += 1
            dp[i+1][j] %= mod
    print(dp[N][S])

main()

