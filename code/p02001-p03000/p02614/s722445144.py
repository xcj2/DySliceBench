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



def paint(i, j, copied):

    for I in range(h):
        if((i>>I)&1):
            for J in range(w):
                copied[I][J] = "$"

    for J in range(w):
        if((j>>J)&1):
            for I in range(h):
                copied[I][J] = "$"

def check(grid1):
    toret = 0
    for i in range(h):
        for j in range(w):
            if(grid1[i][j]=='#'):
                toret+=1
    return (toret==k)

h,w,k = MAP()

grid = []

for _ in range(h):
    grid.append(list(input()))


ans = 0

for row in range(1<<h):
    for col in range(1<<w):
        copied = [x[:] for x in grid]
        paint(row, col, copied)

        ans+=check(copied)
        # print(copied, grid, ans, row, col)
print(ans)