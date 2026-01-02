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


D, N = na()
print(N * 100**D if N != 100 else 101 * 100**D)
