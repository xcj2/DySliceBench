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
h,w,k=MI()
lis=[[0]*w for i in range(h)]
for i in range(h):
    s=SI()
    for j in range(w):
        if s[j]=="#":
            lis[i][j]=1
#print(lis)
ans=0
for x in product([0,1],repeat=h+w):
    count=0
    for i in range(h):
        for j in range(w):
            if x[i]==0 and x[h+j]==0 and lis[i][j]==1:
                count+=1
    if count==k:
        ans+=1
print(ans)
    