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
    inf=10**6
    n,m=MI()
    cc=LI()
    dp=[inf]*(n+1)
    dp[0]=0
    for c in cc:
        for i in range(n-c+1):
            if dp[i]==inf:continue
            if dp[i]+1<dp[i+c]:dp[i+c]=dp[i]+1
    print(dp[-1])

main()

