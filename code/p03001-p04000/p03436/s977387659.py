# coding: utf-8
# hello worldと表示する
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
lis=[[0]*(w+2) for i in range(h+2)]
for i in range(h):
    s=SI()
    for j in range(w):
        if s[j]==".":
            lis[i+1][j+1]=1
#print(lis)
step=[[1,0],[0,-1],[-1,0],[0,1]]
counter=[[-1]*(w+2) for i in range(h+2)]
counter[1][1]=0
q=deque([[1,1]])
while q:
    x,y=q.popleft()
    #print(x,y)
    for i,j in step:
        if counter[x+i][y+j]<0 and lis[x+i][y+j]==1:
            q.append([x+i,y+j])
            counter[x+i][y+j]=counter[x][y]+1
if counter[h][w]<0:
    print(-1)
    sys.exit()
white=0
for i in range(h+2):
    white+=sum(lis[i])
#print(white)
if lis[1][1]==1:
    white-=1
ans=white-counter[h][w]
print(ans)
#print(counter[h][w])
