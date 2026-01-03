#!/usr/bin/env python3
#ABC44 D

import sys
import math
import bisect
import time
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

#√n < bの場合はnをb進数表記すると2桁になることに着目
n = I()
s = I()
def f(b,n):
    if n < b:
        return n
    else:
        return f(b,n//b) + n % b

if n == s:
    print(n+1)
    quit()
for b in range(2,int(math.sqrt(n))+1):
    if f(b,n) == s:
        print(b)
        quit()
for p in range(1,int(math.sqrt(n))+1)[::-1]:
    b = (n-s)//p + 1
    if b <= 1:
        continue
    if f(b,n) == s:
        print(b)
        quit()
print(-1)
