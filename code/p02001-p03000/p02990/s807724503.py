import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
#from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [LI()for i in range(n)]
inf = 10**17
mod = 10**9 + 7

import math
def comb(n, r):
    if n<0 or r<0 or n<r:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def comod(n,r):
    return comb(n,r)%mod

n,k=MI()
ans=[0 for i in range(k)]
b=k
r=n-k
for i in range(1,k+1):
    #ans[i-1]=2*comod(b-1,i-1)*comod(r-1,i-1)+comod(b-1,i-1)*comod(r-1,i)+comod(b-1,i-1)*comod(r-1,i-2)
    ans[i-1]=comod(n-k+1,i)*comod(k-1,i-1)

#print(ans)
for a in ans:
    print(a%mod)
