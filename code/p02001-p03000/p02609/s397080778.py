import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N = INT()
X = input()

def popcount(n):
    cnt = 0
    while n:
        n %= "{:b}".format(n).count("1")
        cnt += 1
    return cnt

pl = [0]*(N+1)
for i in range(N+1):
    pl[i] = popcount(i)
bn = X.count("1")

modp = [0]*N
modm = [0]*N

for i in range(N):
    if X[i] == "1":
        modp[i] = pow(2, N-1-i, bn+1)
        if not bn == 1:
            modm[i] = pow(2, N-1-i, bn-1)

sp = sum(modp)
sm = sum(modm)
ans = [0]*N
for i in range(N):
    if X[i] == "1":
        if bn == 1:
            ans[i] = 0
            continue
        s = sm
        s -= modm[i]
        s %= bn-1
        ans[i] = pl[s]+1
    else:
        s = sp
        s += pow(2, N-1-i, bn+1)
        s %= bn+1
        ans[i] = pl[s]+1

print(*ans, sep="\n")
