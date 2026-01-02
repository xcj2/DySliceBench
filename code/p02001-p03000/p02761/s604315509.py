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


n, m = na()

if n == 3:
    ans = [-1, -1, -1]
    for _ in range(m):
        s, c = na()
        if ans[s - 1] == -1:
            ans[s - 1] = c
        else:
            if ans[s - 1] != c:
                print(-1)
                quit()
    if ans[0] == 0:
        print(-1)
        quit()
    print(ans[0] if ans[0] != -1 else 1, end="")
    for i in range(1, 3):
        print(ans[i] if ans[i] != -1 else 0, end="")
    print()
elif n == 2:
    ans = [-1, -1]
    for _ in range(m):
        s, c = na()
        if ans[s - 1] == -1:
            ans[s - 1] = c
        else:
            if ans[s - 1] != c:
                print(-1)
                quit()
    if ans[0] == 0:
        print(-1)
        quit()
    print(ans[0] if ans[0] != -1 else 1, end="")
    for i in range(1, 2):
        print(ans[i] if ans[i] != -1 else 0, end="")
    print()
else:
    ans = [-1]
    for _ in range(m):
        s, c = na()
        if ans[s - 1] == -1:
            ans[s - 1] = c
        else:
            if ans[s - 1] != c:
                print(-1)
                quit()
    print(ans[0] if ans[0] != -1 else 0, end="")
    print()
