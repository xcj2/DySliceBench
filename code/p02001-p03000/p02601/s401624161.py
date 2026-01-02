# Template 1.0
import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log,floor
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

a,b,c = MAP()

k = INT()

z = 0

for i in range(100):
    if(b>a):
        break
    b*=2
    z+=1

for i in range(1000):
    if(c>b):
        break
    c*=2
    z+=1
# print(z)
if(z<=k):
    print("Yes")
else:
    print("No")



# temp = floor(log(a/b, 2))+1
# if(temp>0):
#     b=b*(2**temp)
#
# temp1 = floor(log(b/c, 2))+1
# # print(temp, b, temp1)
# if(temp+temp1<=k):
#     print("Yes")
# else:
#     print("No")