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


x = ni()


def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


for ans in range(x, 10**5 + 4):
    if is_prime(ans):
        print(ans)
        break
