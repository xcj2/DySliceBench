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

n=I()
lis=LI()
lis2=sorted(lis)
pm=[-1 for i in range(n)]
for i in range(n):
    if lis2[i]>=0:
        pm[i]=1
if pm[0]==1:
    pm[0]=-1
elif pm[-1]==-1:
    pm[-1]=1
ans=0
for i in range(n):
    ans=ans+pm[i]*lis2[i]
print(ans)
x=lis2[0]
for i in range(1,n-1):
    if pm[i]==1:
        print(x,lis2[i])
        x=x-lis2[i]
for i in range(1,n-1):
    if pm[i]==-1:
        print(lis2[-1],lis2[i])
        lis2[-1]=lis2[-1]-lis2[i]
print(lis2[-1],x)
    
        


            
        
        
            
    
            
            

    
    
            
            

