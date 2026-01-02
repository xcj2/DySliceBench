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

'''
1,2,3,4,5,6,7,8,9,10,11,12,21,22,23,32,33,34,43,44,45,54,55,56,65,66,67,76,77,78,87,88,89,98,99,100 (36)
101,110,111,112,121,122,123,210,211,212,221,222,223,232,233,234,

1
10
11
12
100
101
110
111
112
121
122
123
1000
1001
1002


'''
#precomp:
nums = []
def precomp(i):
    temp = str(i)
    x=[-1,0,1]
    for j in range(3):
        foo = int(temp[-1])+x[j]
        if(foo>=0 and foo<=9):
            toadd = int(temp+str(foo))

            if (i > 3234566667):
                return
            nums.append(toadd)
            precomp(toadd)

for i in range(1, 10):
    nums.append(i)
    precomp(i)

nums.sort()

k = INT()

print(nums[k-1])

# k = INT()
