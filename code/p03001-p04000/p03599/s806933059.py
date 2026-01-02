# coding: utf-8
# hello worldと表示する
import sys
#import numpy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
from copy import deepcopy
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

a,b,c,d,e,f=MI()
wasser=[]
g=f//100
for i in range(int(f/a)+1):
    for j in range(int(f/a)+1):
        if a*i+b*j<=f//100:
            wasser.append(100*(a*i+b*j))
water=list(set(wasser))
water.sort()
#print(water)
sugar=[]
for x in water:
    sugar.append((min(f-x,e*x//100)))
#print(sugar)
sugmx=[]
for s in sugar:
    mx=0
    for i in range(s//c+1):
        for j in range(s//c+1):
            if mx<=c*i+d*j<=s:
                mx=c*i+d*j
    sugmx.append(mx)
#print(sugmx)
mix=-inf
for i in range(1,len(water)):
    u=sugmx[i]/water[i]
    #print(u)
    if u>=mix:
        mix=u
        ans1=sugmx[i]
        ans2=water[i]
print(ans2+ans1,ans1)

