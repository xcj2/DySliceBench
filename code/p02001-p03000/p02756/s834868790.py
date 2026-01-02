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

s = deque(ns())
q = ni()
now = 1
for i in range(q):
    qu = ns().split()
    if qu[0] == "1":
        now *= -1
    else:
        if qu[1] == "1":
            r = 1
        else:
            r = -1
        if r * now == 1:
            s.appendleft(qu[-1])
        else:
            s.append(qu[-1])
if now == -1:
    s.reverse()
print(*s, sep="")