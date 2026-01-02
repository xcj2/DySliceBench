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

n = INT()
h = LIST()

dp = [0]*n
dp[1] = abs(h[1]-h[0])

for i in range(2,n):
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2]+ abs(h[i] - h[i-2]))

print(dp[n-1])
