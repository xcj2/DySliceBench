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
a = []
b = []
c = []
for i in range(n):
    a1, b1, c1 = MAP()
    a.append(a1)
    b.append(b1)
    c.append(c1)

dp0 = [0]*3
dp1 = [0]*3
dps = [dp0, dp1]
dp = [0]*n
abc = [a, b, c]

dps[0][0] = a[0]
dps[0][1] = b[0]
dps[0][2] = c[0]

dp[0] = max(dps[0])

for i in range(1,n):
    for j in range(3):
        dps[i%2][j] = abc[j][i] + max(dps[(i-1)%2][(j+1)%3], dps[(i-1)%2][(j+2)%3])
    dp[i] = max(dps[i%2])

print(dp[n-1])
