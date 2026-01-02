#!/usr/bin/env python3
#ABC141 E
#Z-algorithm

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
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

def z_algorithm(s):
    n = len(s)
    Z = [0] * n
    Z[0] = n
    L,R = 0,0
    for i in range(1, n):
        if i >= R: #過去の結果が使えない
            L = R = i
            while R < n and s[R-L] == s[R]:
                R += 1
            Z[i] = R - L
        elif Z[i-L] < R-i:#過去の結果が全て使える
            Z[i] = Z[i - L]
        else:#過去の結果が一部使える
            L = i
            while R < n and s[R-L] == s[R]:
                R += 1
            Z[i] = R - L
    return Z

n = I()
s = input()
ans = 0
for i in range(n):
    Z = z_algorithm(s[i:])
    for j,z in enumerate(Z):
        if j < z:
            continue
        ans = max(ans,z)
print(ans)