# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
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

n, m = MAP()

h = LIST()
dd = dict()
for _ in range(m):
    a, b = MAP()
    if(a in dd):
        dd[a].append(b)
    else:
        dd[a] = []
        dd[a].append(b)
    if(b in dd):
        dd[b].append(a)
    else:
        dd[b] = []
        dd[b].append(a)
ans = 0
for i in range(n):
    if((i+1) in dd):
        temp = dd[i+1]
        flag = 1
        for el in temp:
            if(h[el-1]>=h[i]):
                flag = 0
                break
        if(flag==1):
            ans+=1
    else:
        ans+=1
print(ans)