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

def solve(N,M,p1,p2):
    ans = 0

    for i in range(N):
        left = k - p1[i]

        lo = 0
        hi = M - 1

        temp = (i + 1)

        if (left >= 0):
            while (lo <= hi):
                # print(lo, hi, ans)
                mid = (lo + hi) // 2

                if (p2[mid] > left):
                    hi = mid - 1
                else:
                    lo = mid + 1
                    ans = max(ans, temp + lo)
            ans = max(ans, temp + lo)


    return ans


n,m,k = MAP()

a = LIST()

b = LIST()

prefA = [0]*n
prefA[0] = a[0]

for i in range(1, n):
    prefA[i] = prefA[i-1] + a[i]


pref = [0]*m

pref[0] = b[0]

for i in range(1, m):
    pref[i] = pref[i-1] + b[i]
#
# print(prefA)
# print(pref)

print(max(solve(n,m,prefA,pref), solve(m,n,pref,prefA)))