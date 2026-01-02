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

x,y,a,b,c = MAP()

p = LIST()
q = LIST()
r = LIST()

p = sorted(p)[::-1]
q = sorted(q)[::-1]
r = sorted(r)[::-1]

p = p[:x]
q = q[:y]

new = p+q+r
# print(new)
new = sorted(new)[::-1]

print(sum(new[:x+y]))