# coding: utf-8
# hello worldと表示する
import sys
import numpy
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
n=I()
lisr=[LI() for i in range(n)]
lisb=[LI() for i in range(n)]
#print(lisr)
#print(lisb)
lisr.sort(key=itemgetter(1))
lisb.sort(key=itemgetter(1))
#print(lisr)
#print(lisb)
count=0
for i in range(n):
    x,y=lisb[i]
    mx=-inf
    for j in range(n):
        a,b=lisr[j]
        if b<y and a<x:
            if a>mx:
                mx=a
                pos=j
    #print(mx,pos)
    if mx>-inf:
        count+=1
        lisr[pos][1]=inf
print(count)
#print(lisr)

        
    