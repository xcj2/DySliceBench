#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))


def func(x):
    global cnt
    cnt += 1
    if x % 2:
        if f[3*x+1]: 
            print(cnt)
            quit()
        else:
            f[3*x+1] = 1
            func(3*x+1)
    else:
        if f[x//2]:
            print(cnt)
            quit()
        else:
            f[x//2] = 1
            func(x//2)


s = I()
f = defaultdict(int)
f[s] = 1
cnt = 1
func(s)