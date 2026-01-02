import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
from decimal import Decimal, ROUND_CEILING
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

H, W, M = MAP()

h, w = ZIP(M)
cnt_h = Counter(h)
hm = max(cnt_h.values())
cnt_w = Counter(w)
wm = max(cnt_w.values())
hl = [k for k, v in cnt_h.items() if v == hm]
wl = [k for k, v in cnt_w.items() if v == wm]

s = set()
for h_, w_ in zip(h, w):
    s.add((h_, w_))

ans = hm + wm

for i in hl:
    for j in wl:
        if (i, j) not in s:
            break
    else:
        continue
    break
else:
    ans -= 1
print(ans)
