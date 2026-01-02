from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
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


n = ni()
tnow, xnow, ynow = 0, 0, 0
for _ in range(n):
    t, x, y = na()
    l = abs(xnow - x) + abs(ynow - y)
    if (t - tnow) < l or (t - tnow) % 2 != l % 2:
        print("No")
        quit()
print("Yes")
