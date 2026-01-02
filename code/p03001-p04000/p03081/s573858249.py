#!/usr/bin/env python3
import sys
# from math import *


def input(): return sys.stdin.readline()[:-1]


sys.setrecursionlimit(10**8)
inf = float('inf')
mod = 10**9+7

n, q = map(int, input().split())
s = input()
td = []
for i in range(q):
    td.append(input().split())



def solve_binary1(mid):
    for t, d in td:
        if s[mid] == t:
            mid = mid-1 if d == 'L' else mid+1
        if mid == -1 or mid == n:
            break
    if mid == -1:
        return 1
    else:
        return 0



def binary_search1():
    ok = 0
    ng = n
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if solve_binary1(mid):
            ok=mid
        else:
            ng=mid
    return ok


def solve_binary2(mid):
    for t, d in td:
        if s[mid] == t:
            mid = mid-1 if d == 'L' else mid+1
        if mid == -1 or mid == n:
            break
    if mid == n:
        return 1
    else:
        return 0


def binary_search2():
    ok = n
    ng = 0
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if solve_binary2(mid):
            ok = mid
        else:
            ng = mid
    return ok


#左に集まる中でもっとも右の点を探す
ok1=binary_search1()

#右に集まる中でもっとも左の点を探す
ok2=binary_search2()

# ok2 = n
# left = 0
# right = n
# while left < right:
#     mid = (left+right)//2
#     tmp = mid
#     for t, d in td:
#         if s[tmp] == t:
#             tmp = tmp-1 if d == 'L' else tmp+1
#         if tmp == n or tmp == -1:
#             break
#     if tmp == n:
#         right = mid
#         ok2 = min(ok2, mid)
#     else:
#         left = mid+1

print(max(0, ok2-ok1-1))
# print(ok2,ok1)
# print(ok1)
