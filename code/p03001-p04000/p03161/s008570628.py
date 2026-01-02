import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

n,k=MI()
hs=LI()
dp=[inf for i in range(n)]
dp[0]=hs[0]

for i in range(min(n,k)):
    dp[i]=abs(hs[i]-hs[0])
for i in range(n):
    mn=dp[i]
    for j in range(1,k+1):
        if i-j>=0:
            u=dp[i-j]+abs(hs[i]-hs[i-j])
            if u<mn:
                mn=u
    dp[i]=mn
print(dp[-1])
