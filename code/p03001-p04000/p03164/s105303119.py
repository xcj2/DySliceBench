import sys
from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
import collections
from collections import deque 

input = sys.stdin.readline

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------

N, W = inpl()
INF = 10**12
dp = [[INF] * 100001 for i in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    w, v = inpl()
    for j in range(0, 100001):
        if j - v >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v] + w)
        else:
            dp[i][j] = dp[i-1][j]
            
ans = 100000
while dp[N][ans] > W:
    ans -= 1

_debug(dp[N][ans])
print(ans)