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

def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m,n%m)

def lcm(n,m):
    return n*m // gcd(n,m)


n,m = LI()
a = LI()
b = [i//2 for i in a]

lb = 1
for i in b:
    lb = lcm(lb,i)
    if lb > m:
        print(0)
        quit()

for i in b:
    if lb//i % 2 == 0:
        ans = 0
        break
else:
    ans = (m//lb + 1)//2
print(ans)
