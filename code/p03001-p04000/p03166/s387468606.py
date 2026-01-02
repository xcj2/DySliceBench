import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
import collections
from collections import deque 

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------

N, M = inpl()
graph = [[] for i in range(N+1)]

for i in range(M):
    x, y = inpl()
    graph[x].append(y)

flag = [False] * (N + 1)
dp = [0] * (N + 1)


def f(x):
    if flag[x]:
        return dp[x]
    flag[x] = True
    fans = 0
    for y in graph[x]:
        fans = max(fans, f(y) + 1)
    dp[x] = fans
    return dp[x]

ans = 0
for i in range(1, N + 1):
    ans = max(ans, f(i))
print(ans)
