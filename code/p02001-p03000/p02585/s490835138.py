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
per=LI()
for i in range(n):
    per[i]-=1
points=LI()
ans=-inf
for i in range(n):
    val=0
    #res=[0 for j in range(n+1)]
    res=[]
    pos=per[i]
    inipos=per[i]
    count=0
    while True:
        val+=points[pos]
        pos=per[pos]
        if len(res)==0:
            res.append(val)
        else:
            res.append(max(res[-1],val))
        #res[count]=max(val,res[count-1])
        count+=1
        if pos==inipos:
            break
    loop=(val,count)
    #print(loop)
    #print(res)
    for x in range(len(res)):
        if loop[0]<=0:
            ans=max(ans,res[x])
        else:
            ans=max(ans,res[x]+loop[0]*((k-x-1)//loop[1]))
print(ans)
        
        
        
        
        
        
    
    
    
        
        
        
        
        
            
            