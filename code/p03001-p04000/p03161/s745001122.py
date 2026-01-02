import sys
import fractions
from collections import Counter, deque, defaultdict
from math import factorial
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n, k = MAP()
h = LIST()

dp = [INF]*n
dp[0] = 0

for i in range(1,n):
    for j in range(1,min(i, k)+1):
        dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

print(dp[n-1])
