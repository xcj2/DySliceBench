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

n,k=MI()
lis=LI()
dp=[[0]*(k+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    sm=0
    for j in range(lis[i]+1):
        sm+=dp[i][j]
        dp[i+1][j]=sm%mod
    for j in range(lis[i]+1,k+1):
        sm+=dp[i][j]
        sm-=dp[i][j-lis[i]-1]
        dp[i+1][j]=sm%mod
print(dp[-1][-1]%mod)            
        
    
