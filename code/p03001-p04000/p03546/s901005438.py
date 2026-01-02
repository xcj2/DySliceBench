# coding: utf-8
# hello worldと表示する
#dpでできないかな？
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
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

def warshall_floyd(d):
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d
h,w=MI()
d=[LI() for i in range(10)]
d=warshall_floyd(d)
lis=[LI() for i in range(h)]
ans=0
for i in range(h):
    for j in range(w):
        if lis[i][j]>=0:
            ans+=d[lis[i][j]][1]
print(ans)