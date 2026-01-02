# standard library# {{{
import sys
import os
import time
import re
import string
import math
from operator import itemgetter
from collections import Counter
from collections import deque
from collections import defaultdict as dd
import fractions
from heapq import heappop, heappush, heapify
import array
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy as dcopy
import itertools
sys.setrecursionlimit(10**7)
inf = 10**20
gosa = 1.0 / 10**10
mod = 10**9+7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def DP(N, M, first): return [[first] * M for n in range(N)]
# }}}

# input


def solve():
    N, h = map(int, input().split())
    I = [list(map(int, input().split())) for _ in range(N)]
    A = [x[0] for x in I]
    B = [x[1] for x in I]
    A.sort()
    a = max(A)
    B.sort()
    C = B[bisect_left(B, a):]
    s = sum(C)

    count = 0
    for c in reversed(C):
        count += 1
        h -= c
        if h > 0:
            pass
        else:
            break

    if h > 0:
        count += math.ceil(h/a)

    print(count)

if __name__ == "__main__":
    solve()
