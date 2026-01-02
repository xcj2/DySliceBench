import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
from copy import deepcopy
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
inf = 10**17
mod = 10**9 + 7

h,w=MI()
data=[list(input().rstrip()) for i in range(h)]
#print(data)
deletes=[]
for i in range(h):
    count=0
    for j in range(w):
        if data[i][j]==".":
            count+=1
    if count==w:
        deletes.append(i)
for j in list(reversed(deletes)):
    del data[j]
#print(data)
h-=len(deletes)
data2=[[0 for i in range(h)] for j in range(w) ]
for i in range(w):
    for j in range(h):
        data2[i][j]=data[j][i]
#print(data2)
deletes2=[]
for i in range(w):
    count=0
    for j in range(h):
        if data2[i][j]==".":
            count+=1
    if count==h:
        deletes2.append(i)
for j in list(reversed(deletes2)):
    del data2[j]
w-=len(deletes2)
#print(data2)
data3=[[0 for i in range(w)] for j in range(h)]
#print(h,w)
#print(data3)
for i in range(h):
    for j in range(w):
        data3[i][j]=data2[j][i]
#print(data3)
for i in range(h):
    for j in range(w):
        print(data3[i][j],end="")
    print("")