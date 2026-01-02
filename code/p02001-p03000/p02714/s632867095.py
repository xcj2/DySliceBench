import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def inp():
    return int(input())
def inps():
    return input().rstrip()
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10

# from heapq import heappush, heappop, heapify
# import math
# from math import gcd
# import itertools as it
# import collections
# from collections import deque 

# ---------------------------------------

N = inp()
S = inps()

r = []
g = []
b = []

for i in range(N):
    if S[i] == "R":
        r.append(i)
    if S[i] == "G":
        g.append(i)
    if S[i] == "B":
        b.append(i)

ans = 0
for i in r:
    for j in g:
        m = i
        n = j
        if m > n:
            m, n = n, m
        sa = abs(m - n)
        ans += len(b)
        if m - sa >= 0 and S[m - sa] == "B":
            ans -= 1
        if n + sa < N and S[n + sa] == "B":
            ans -= 1
        if sa % 2 == 0 and S[m + sa//2] == "B":
            ans -= 1
print(ans)
