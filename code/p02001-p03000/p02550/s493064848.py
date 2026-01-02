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

n,x,m = MAP()

temp = [x]

present = [-1]*(m+1)

present[x] = 0

i,j = -1, -1

for iter in range(1, n):
    new = (temp[-1]**2)%m
    if(present[new]==-1):
        temp.append(new)
        present[new] = iter
    else:
        i = present[new]
        j = iter
        break
    # print(temp)
# print(i,j)
if(i!=-1):
    sum1 = sum(temp[:i])
    left = n-i
    sum2 = sum(temp[i:j])
    zz = j-i
    sum1+=sum2*(left//zz)
    still = left%zz
    while(still>0):
        sum1+=temp[i]
        i+=1


        still-=1
else:
    sum1 = sum(temp)
print(sum1)