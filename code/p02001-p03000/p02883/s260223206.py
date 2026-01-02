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
from math import floor, ceil,pi,factorial,sqrt
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

def ceiler(a,b):
    return -((-a)//b)
n,k=MI()
costs=LI()
difs=LI()
costs.sort()
difs.sort(reverse=True)
lis=[0 for i in range(n)]
#print(costs)
#print(difs)
for i in range(n):
    lis[i]=costs[i]*difs[i]
#print(lis)
def judge(x):
    times=0
    for i in range(n):
        u=ceiler(lis[i]-x,difs[i])
        times+=max(0,u)
        #print(u)
    #print(x,times<=k)
    return times<=k
l,r=-1,10**13
while l+1<r:
    mid=(l+r)//2
    if judge(mid):
        r=mid
    else:
        l=mid
print(r)
    
    

    


    
 


