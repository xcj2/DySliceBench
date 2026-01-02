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

def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

n = I()
lst = ['a','b','c','d','e','f','g','h','i','j']
cnt = n
ans = []

def dfs(s,num,kinds):
    if num == n:
        ans.append(s)
        return
    for i in range(kinds+1):
        if lst[i] in s:
            dfs(s+lst[i],num+1,kinds)
        else:
            dfs(s+lst[i],num+1,kinds+1)
    return 

dfs('',0,0)

for i in ans:
    print(i)

