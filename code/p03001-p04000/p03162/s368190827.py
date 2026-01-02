from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
mod2 = 998244353
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpln(n): return list(int(sys.stdin.readline()) for i in range(n))

n = inp()
abc = [inpl() for i in range(n)]
dp = [[0] * 3 for i in range(n+5)]
for i in range(3):
    dp[0][i] = abc[0][i]
for i in range(n-1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][j] = max(dp[i+1][j], dp[i][k] + abc[i+1][j])
print(max(dp[n-1]))