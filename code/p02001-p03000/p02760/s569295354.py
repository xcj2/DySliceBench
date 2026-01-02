# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

grid = []

for _ in range(3):
    grid.append(LIST())

n =INT()

for _ in range(n):
    b = INT()
    for i in range(3):
        for j in range(3):
            if(grid[i][j]==b):
                grid[i][j] = -1
flag = 0
for i in range(3):
    if(sum(grid[i])==-3):
        flag = 1
        break
if(flag==0):
    for i in range(3):
        temp = 0
        for j in range(3):
            temp+=grid[j][i]
        if(temp==-3):
            flag= 1
            break
if(flag==0):
    temp = 0
    for i in range(3):
        temp+=grid[i][i]
    if(temp==-3):
        flag = 1
if(flag==0):
    temp = 0
    for i in range(3):
        temp += grid[i][2-i]
    if (temp == -3):
        flag = 1
if(flag==1):
    print("Yes")
else:
    print("No")