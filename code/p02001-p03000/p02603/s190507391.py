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

n = INT()

a = LIST()

curr = 1000

st = 0

for i in range(1, n):
    if(a[i]>a[i-1]):
        if(curr>0):
            temp = curr//a[i-1]
            st+=temp
            curr-=temp*a[i-1]
    elif(a[i]<a[i-1]):
        if(st>0):
            curr+=st*a[i-1]
            st = 0

if(st>0):
    curr+=st*a[-1]
print(curr)