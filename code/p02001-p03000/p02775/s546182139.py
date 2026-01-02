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

def main():
    N = S()[::-1] + '0'
    dp = [[0 for _ in range(2)] for _ in range(len(N)+1)]
    dp[0][1] = inf
    for d_i in range(len(N)):
        digit = int(N[d_i])
        i = d_i + 1
        dp[i][0] = min(
            dp[i-1][0] + digit,
            dp[i-1][1] + digit + 1,
        )
        dp[i][1] = min(
            dp[i-1][0] + (10 - digit),
            dp[i-1][1] + (10 - (digit + 1))
        )
    print(dp[len(N)][0])

main()

