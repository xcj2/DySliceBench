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

n=I()
ans=0
lis=[I() for i in range(n)]
ind =[0 for i in range(n)]
for i in range(n):
    if lis[i]==0:
        ind[i]=-1
    ans+=lis[i]//2
    lis[i]=lis[i]%2
points=[]
for i in range(n):
    if lis[i]==1:
        points.append(i)
#print(points)
#for i in range(len(points)-1):
z=0
while z<len(points)-1:
    x=points[z]
    y=points[z+1]
    count=0
    #print(y)
    #print(x)
    for j in range(x,y+1):
        if ind[j]==0:
            count+=1
    if count==y-x+1:
        z+=1
        ans+=1
    z+=1
print(ans)
    






        
        
    
    
        
    
    
