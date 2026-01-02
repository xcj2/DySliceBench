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

n, k =MAP()

a = LIST()

# vis = [False]*n
# idx = 0
# temp = [a[0]-1]
# vis[a[0]-1] =True
i=0
j = 1
dd = defaultdict(int)
dd[1] = 0
while(True):
    if(a[i] in dd):
        pos = dd[a[i]]
        break
    dd[a[i]] = j
    i = a[i]-1
    j+=1

suited = list(dd.keys())[pos:]
temp = j-pos
if(k>=pos):
    k-=pos
    k = k%temp

    print(suited[k])
else:
    newS = list(dd.keys())[:pos]
    print(newS[k])