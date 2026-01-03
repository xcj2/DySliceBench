# coding: utf-8
# hello worldと表示する
#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial,sqrt
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7

w,h,n=MI()
xmx=w
ymx=h
xmn=0
ymn=0
for i in range(n):
    x,y,a=MI()
    if a==2:
        xmx=min(x,xmx)
    if a==1:
        xmn=max(x,xmn)
    if a==4:
        ymx=min(y,ymx)
    if a==3:
        ymn=max(y,ymn)
    #print(xmn,xmx,ymn,ymx)
print(max(xmx-xmn,0)*max(ymx-ymn,0))