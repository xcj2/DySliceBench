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
def _dbg(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------

N, K = inpl()
h = inpl()

INF = 10**10

dp = [INF] * N
dp[0] = 0

for j in range(1, N):
    for step in range(1, min(K, j)+1):
        dp[j] = min(dp[j], dp[j-step] + abs(h[j] - h[j-step]))
    _dbg(dp[1])

print(dp[N-1])