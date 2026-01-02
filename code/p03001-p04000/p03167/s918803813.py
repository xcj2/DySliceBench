#BFSにdpを乗っける
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

h,w=MI()
lis=[[0]*w for i in range(h)]
for i in range(h):
    s=SI()
    for j in range(w):
        if s[j]=="#":
            lis[i][j]=1
#print(lis)
Q=deque([[0,0]])
dp=[[-1]*w for i in range(h)]
dp[0][0]=1
step=[[1,0],[0,1]]
while Q:
    x,y=Q.popleft()
    for i,j in step:
        if x+i>=h or y+j>=w:
            continue
        if lis[x+i][y+j]==1:
            continue
        if dp[x+i][y+j]<0:
            dp[x+i][y+j]=dp[x][y]%mod
            Q.append([x+i,y+j])
        else:
            dp[x+i][y+j]+=dp[x][y]%mod
    #print(dp)
print(max(0,dp[-1][-1])%mod)
    

        