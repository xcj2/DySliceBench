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
    H, W = LI()
    g = []
    for _ in range(H):
        g.append(S())
    dp = [[inf for _ in range(W)] for __ in range(H)]

    if g[0][0] == '#':
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    for r in range(H):
        for c in range(W):
            if r != H-1:
                if g[r][c] == '.' and g[r+1][c] == '#':
                    dp[r+1][c] = min(dp[r+1][c], dp[r][c] + 1)
                else:
                    dp[r+1][c] = min(dp[r+1][c], dp[r][c])
            if c != W-1:
                if g[r][c] == '.' and g[r][c+1] == '#':
                    dp[r][c+1] = min(dp[r][c+1], dp[r][c] + 1)
                else:
                    dp[r][c+1] = min(dp[r][c+1], dp[r][c])
    print(dp[-1][-1])
main()

