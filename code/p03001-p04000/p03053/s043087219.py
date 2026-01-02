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
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

h,w=MI()
dp=[[-1]*w for i in range(h)]
Q=deque([])
for i in range(h):
    s=SI()
    for j in range(w):
        if s[j]=="#":
            dp[i][j]=0
            Q.append((i,j))
step=[(-1,0),(1,0),(0,1),(0,-1)]
while Q:
    x,y=Q.popleft()
    for i,j in step:
        if not(0<=x+i<h and 0<=y+j<w):
            continue
        if dp[x+i][y+j]<0:
            Q.append((x+i,y+j))
            dp[x+i][y+j]=dp[x][y]+1
ans=-inf
#print(dp)
for i in range(h):
    for j in range(w):
        ans=max(ans,dp[i][j])
print(ans)
            
    
        

    
        


            
        
        
            
    
            
            

    
    
            
            

