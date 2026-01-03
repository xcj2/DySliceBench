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

n,c,k=MI()
time=[I() for i in range(n)]
time.sort()
lis=[[time[i],time[i]+k] for i in range(n)]
#print(lis)
i=0
ans=0
count=0
while i<n:
    if count==c:
        count=0
        ans+=1
        #print("1x")
    elif count==0:
        count=1
        sup=lis[i][1]
        i+=1
        #print("2x")
    elif count<c:
        if lis[i][0]>sup:
            ans+=1
            count=0
            #print("3x")
        else:
            count+=1
            i+=1
            #print("4x")
    #print(sup)
if count!=0:
    ans+=1
    
print(ans)
            
            
    
    