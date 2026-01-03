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

dp = [[[0 for _ in range(51)] for __ in range(2501)] for ___ in range(51)]

def main():
    N, A = LI()
    X = LI()
    dp[0][0][0] = 1
    # for i in range(51):
    #     dp[i][0][0] = 1

    for i in range(N):
        for j in range(2501):
            for k in range(N+1):
                if j - X[i] >= 0 and k - 1 >= 0:
                    dp[i+1][j][k] += dp[i][j-X[i]][k-1]
                dp[i+1][j][k] += dp[i][j][k]
    cnt = 0
    for k in range(1, N+1):
        cnt += dp[N][k*A][k]
    print(cnt)
main()

