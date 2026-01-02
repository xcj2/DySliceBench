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


a = list()
for _ in range(3):
    a = a + na()
n = ni()
t = [0 for _ in range(9)]
for _ in range(n):
    b = ni()
    for i, ai in enumerate(a):
        if ai == b:
            t[i] = 1

ans = "No"
for i in range(3):
    if t[3 * i] + t[3 * i + 1] + t[3 * i + 2] == 3:
        ans = "Yes"
    if t[0 + i] + t[3 + i] + t[6 + i] == 3:
        ans = "Yes"
if t[0] + t[4] + t[8] == 3:
    ans = "Yes"
if t[2] + t[4] + t[6] == 3:
    ans = "Yes"
print(ans)
