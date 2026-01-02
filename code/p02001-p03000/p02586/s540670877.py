from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,m,k = inpl()
value = [[0 for _ in range(m)] for i in range(n)]
for _ in range(k):
    a,b,c = inpl()
    value[a-1][b-1] = c
dp = [0] * (4*(m+1)*(n+1))
def ind(i,j,k): 
    return 4*(m+1)*i + 4*j + k
for i in range(n):
    for j in range(m):
        for k in range(3)[::-1]:
            dp[ind(i,j,k+1)] = max(dp[ind(i,j,k+1)], dp[ind(i,j,k)] + value[i][j])
        for k in range(4):
            dp[ind(i+1,j,0)] = max(dp[ind(i+1,j,0)], dp[ind(i,j,k)])
            dp[ind(i,j+1,k)] = max(dp[ind(i,j+1,k)], dp[ind(i,j,k)])
# print(dp)
mx = 0
for k in range(4):
    mx = max(mx, dp[ind(n-1,m-1,k)])
print(mx)