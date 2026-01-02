#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
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
lis=[list(SI()) for i in range(h)]
al=[[-1]*w for i in range(h)]
dp=[[inf]*w for i in range(h)]
'''for i in range(h):
    for j in range(w):
        if lis[i][j]=="#":
            dp[i][j]=-1'''
dp[0][0]= 0 if lis[0][0]=="." else 1
q=deque([[0,0]])
step=[[0,1],[1,0]]
#print(lis)
while q:
    x,y=q.popleft()
    if lis[x][y]==".":
        state=1
    else:
        state=-1
    for i,j in step:
        if x+i>h-1 or y+j>w-1:
            continue
        elif state==1:
            if al[x+i][y+j]<0:
                al[x+i][y+j]=0
                q.append([x+i,y+j])
            if lis[x+i][y+j]=="#":
                dp[x+i][y+j]=min(dp[x+i][y+j],dp[x][y]+1)
            else:
                dp[x+i][y+j]=min(dp[x+i][y+j],dp[x][y])
        elif state==-1:
            if al[x+i][y+j]<0:
                al[x+i][y+j]=0
                q.append([x+i,y+j])
            dp[x+i][y+j]=min(dp[x+i][y+j],dp[x][y])
print(dp[-1][-1])