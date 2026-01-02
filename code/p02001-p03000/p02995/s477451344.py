#!/usr/bin/env python3
#ABC131 C

import sys
import math
import bisect
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

def gcd(n,m):
    if m == 0:
        return n
    else:
        return gcd(m,n%m)
def lcm(n,m):
    return (n*m)//gcd(n,m)

a,b,c,d = LI()
i,j,k = (a-1)//c,(a-1)//d,(a-1)//lcm(c,d)
s,t,u = b//c,b//d,b//lcm(c,d)
x = b - s - t + u
y = (a-1) - i - j + k
print(x -y)
