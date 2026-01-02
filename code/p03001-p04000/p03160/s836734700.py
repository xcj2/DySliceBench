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
a = inpl()
dp = [INF] * (n+5)
dp[0] = 0
for i in range(n-1):
    dp[i+1] = min(dp[i+1], dp[i] + abs(a[i+1]-a[i]))
    if i != n-2:
        dp[i+2] = min(dp[i+2], dp[i] + abs(a[i+2]-a[i]))
print(dp[n-1])