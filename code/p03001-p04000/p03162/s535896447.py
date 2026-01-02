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

N = inp()
a = [0] * N
b = [0] * N
c = [0] * N
for i in range(N):
    a[i], b[i], c[i] = inpl()

dp = [[0] * 3 for i in range(N)]
dp[0][0], dp[0][1], dp[0][2] = a[0], b[0], c[0]

for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i]
    dp[i][1] = max(dp[i-1][2], dp[i-1][0]) + b[i]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c[i]
_debug(dp)

mx = 0
for i in dp[N-1]:
    mx = max(mx, i)

print(mx)
