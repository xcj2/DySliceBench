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


def findMaximum(low, high):
    # Base Case: Only one element is present in arr[low..high]*/
    if low == high:
        return fun(low)

        # If there are two elements and first is greater then
    # the first element is maximum */
    if high == low + 1 and fun(low) >= fun(high):
        return fun(high);

        # If there are two elements and second is greater then
    # the second element is maximum */
    if high == low + 1 and fun(low) < fun(high):
        return fun(low)

    mid = (low + high) // 2  # low + (high - low)/2;*/

    # If we reach a point where arr[mid] is greater than both of
    # its adjacent elements arr[mid-1] and arr[mid+1], then arr[mid]
    # is the maximum element*/
    if fun(mid) <= fun(mid+1) and fun(mid) <= fun(mid-1):
        return fun(mid)

        # If arr[mid] is greater than the next element and smaller than the previous
    # element then maximum lies on left side of mid */
    if fun(mid) >= fun(mid+1) and fun(mid) <= fun(mid-1):
        return findMaximum(mid+1,high)
    else:  # when arr[mid] is greater than arr[mid-1] and smaller than arr[mid+1]
        return findMaximum(low, mid-1)

def fun(zz):
    return abs(x+d*(2*zz-k))

x,k,d = MAP()

l = 0
r = k

print(findMaximum(l, r))