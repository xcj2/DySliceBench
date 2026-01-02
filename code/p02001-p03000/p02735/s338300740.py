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
            if r == 0 and c == 0:
                if g[r][c] == '#':
                    dp[r][c] = 1
                else:
                    dp[r][c] = 0
 
            cand1, cand2 = inf, inf
            if 0 <= r-1 < H:
                if g[r-1][c] == '.' and g[r][c] == '#':
                    dp[r][c] = min(dp[r][c], dp[r-1][c] + 1)
                else:
                    dp[r][c] = min(dp[r][c], dp[r-1][c])
            if 0<= c-1 < W:
                if g[r][c-1] == '.' and g[r][c] == '#':
                    dp[r][c] = min(dp[r][c], dp[r][c-1] + 1)
                else:
                    dp[r][c] = min(dp[r][c], dp[r][c-1])
    print(dp[-1][-1])
main()

