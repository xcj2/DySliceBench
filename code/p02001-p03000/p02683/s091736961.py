# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
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

def solve(idx, cur, cost):
    #####
    if(idx==n):
        # print(cur)
        flag = 0
        for el in cur:
            if(el<x):
                flag = 1
                break
        if(flag==0):
            return cost
        else:
            return INF

    cur1 = [0]*m
    for i, el in enumerate(a[idx]):
        cur1[i] += el+cur[i]
    temp1 = solve(idx+1, cur1, cost+c[idx])
    temp2 = solve(idx+1, cur, cost)

    return min(temp1, temp2)

n,m,x = MAP()

c = []
a = []

for _ in range(n):
    temp = LIST()
    c.append(temp[0])
    a.append(temp[1:])

curr = [0]*m
ans = solve(0, curr, 0)
if(ans==INF):
    print(-1)
else:
    print(ans)