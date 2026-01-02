import sys

sys.setrecursionlimit(10 ** 6)
from bisect import *
from collections import *
from heapq import *

int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline()[:-1]
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def MF(): return map(float, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI1(): return list(map(int1, sys.stdin.readline().split()))
def LF(): return list(map(float, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
dij = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def main():
    s=SI()
    t=SI()
    n=len(s)
    m=len(t)
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):dp[i][0]=i
    for j in range(m+1):dp[0][j]=j
    for i,c0 in enumerate(s):
        for j,c1 in enumerate(t):
            dp[i+1][j+1]=min(dp[i][j+1]+1,dp[i+1][j]+1,dp[i][j]+(c0!=c1))
    print(dp[n][m])

main()

