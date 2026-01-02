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

n,m = MAP()

a = ["-1"]*n
flag = 0

if(n==1 and m==0):
    print(0)
else:
    for _ in range(m):
        s,c = MAP()
        c = str(c)
        if(a[s-1]=="-1" or a[s-1]==c):
            a[s-1] = c
        else:
            flag = 1
            break
    if(flag==1):
        print(-1)
    else:
        ans = 0
        if(a[0]=="-1"):
            a[0] = "1"

        for i in range(1, n):
            if(a[i]=="-1"):
                a[i] = "0"
        ans = int("".join(a))
        # print(ans)
        if(len(str(ans))==n):
            print(ans)
        else:
            print(-1)