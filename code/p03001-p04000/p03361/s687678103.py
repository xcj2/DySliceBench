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
lis=[[0 for i in range(w+2)] for j in range(h+2)]
for i in range(h):
    u=list(input().rstrip())
    #print(u)
    for j in range(w):
        if u[j]=="#":
            lis[i+1][j+1]=1
step=[[1,0],[-1,0],[0,1],[0,-1]]
#print(lis)
for i in range(1,h+1):
    for j in range(1,w+1):
        if lis[i][j]==1:
            count=0
            for x,y in step:
                if lis[i+x][j+y]==1:
                    count+=1
            if count==0:
                print("No")
                sys.exit()
print("Yes")