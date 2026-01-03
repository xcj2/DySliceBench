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


n = ni()
a = na()

a.sort(reverse=True)
l = list()
for key, gr in groupby(a):
    if len(l) == 2:
        break
    num = len(list(gr))
    if num >= 2:
        l.append(key)
    if num >= 4:
        l.append(key)
print(l[0] * l[1] if len(l) >= 2 else 0)
