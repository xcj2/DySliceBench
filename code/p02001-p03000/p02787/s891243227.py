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

h,n=MI()
lis=[LI() for i in range(n)]
mx=sorted(lis,reverse=True)[0][0]
#print(mx)
dp=[0 for i in range(h+mx)]
for i in range(1,h+mx):
    mn=inf
    #print(i,i)
    for j in range(n):
        u=dp[max(i-lis[j][0],0)]+lis[j][1]
        #print(u)
        if u<mn:
            mn=u
    dp[i]=mn
#print(dp)
z=[]
for i in range(mx):
    z.append(dp[h+i])
print(min(z))