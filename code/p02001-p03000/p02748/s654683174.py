from itertools import accumulate, permutations, combinations, product, combinations_with_replacement, groupby
from math import sqrt, factorial, log
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heappushpop
import sys
stdin = sys.stdin
mod = 10**9 + 7

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

A, B, M = na()
a = na()
b = na()
ans = min(a) + min(b)
for i in range(M):
    x, y, c = na()
    x -= 1
    y -= 1
    ans = min(ans, a[x]+b[y]-c)
print(ans)
