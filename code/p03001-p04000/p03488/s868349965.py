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
from math import floor, ceil,pi,factorial,sqrt
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

s=input().rstrip().split("T")
x,y=MI()
#print(s)
lisx=[]
lisy=[]
x-=len(s[0])
for i in range(1,len(s)):
    if i%2==0:
        lisx.append(len(s[i]))
    else:
        lisy.append(len(s[i]))
resx=[[] for i in range(len(lisx)+1)]
resy=[[] for i in range(len(lisy)+1)]
resx[0]=[0]
resy[0]=[0]
#print(lisx)
for i in range(len(lisx)):
    for j in range(len(resx[i])):
        resx[i+1].append(resx[i][j]+lisx[i])
        resx[i+1].append(resx[i][j]-lisx[i])
    resx[i+1]=list(set(resx[i+1]))
#print(resx)
for i in range(len(lisy)):
    for j in range(len(resy[i])):
        resy[i+1].append(resy[i][j]+lisy[i])
        resy[i+1].append(resy[i][j]-lisy[i])
    resy[i+1]=list(set(resy[i+1]))
#print(lisy)
#print(resy)
if x in resx[-1] and y in resy[-1]:
    print("Yes")
else:
    print("No")
    

        
        
        
            
        

                