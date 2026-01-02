# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

k=I()
dpmod=[0 for i in range(10**6+100)]
dpmod[0]=7%k
for i in range(10**6+100-1):
    dpmod[i+1]=(10*dpmod[i])%k
dp=[0 for i in range(10**6+100)]
dp[0]=7%k
for i in range(10**6+100-1):
    if dp[i]%k==0:
        print(i+1)
        sys.exit()
    dp[i+1]=dp[i]+dpmod[i+1]
print(-1)
    
    
    


