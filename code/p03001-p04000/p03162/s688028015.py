from collections import defaultdict,deque
import numpy as np
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N = inp()
abc = [inpl() for _ in range(N)]
dp = [[0]*3 for _ in range(N)]
dp[0] = abc[0]

for i in range(1,N):
    a,b,c = abc[i]
    dp[i][0] = max(dp[i-1][1],dp[i-1][2])+a
    dp[i][1] = max(dp[i-1][2],dp[i-1][0])+b
    dp[i][2] = max(dp[i-1][0],dp[i-1][1])+c

print(max(dp[-1]))
