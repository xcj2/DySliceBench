from itertools import accumulate, permutations, combinations, product, combinations_with_replacement, groupby
from math import floor, ceil, sqrt, factorial, log
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
from heapq import heappop, heappush, heappushpop
from itertools import product
import sys
stdin = sys.stdin
mod = 10**9 + 7


def ns(): return stdin.readline().rstrip()


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


k, s = na()
ans = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if z >= 0 and z <= k:
            ans += 1
print(ans)
