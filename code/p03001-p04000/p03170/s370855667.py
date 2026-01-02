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
dp=[-1 for i in range(k+1)]
for i in range(lis[0]):
    dp[i]=0
def memo(x):
    if dp[x]!=-1:
        return dp[x]
    else:
        for i in range(n):
            if x-lis[i]<0:
                continue
            elif dp[x-lis[i]]!=-1:
                if dp[x-lis[i]]==0:
                    dp[x]=1
                    return 1
            else:
                if memo(x-lis[i])==0:
                    dp[x]=1
                    return 1
        dp[x]=0
        return 0
for i in range(k+1):
    memo(i)
#print(dp)
if dp[-1]==0:
    print("Second")
else:
    print("First")
            
