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

a,b,c,x,y=MI()
if a+b<=2*c:
    ans=a*x+b*y
else:
    if x>=y:
        if a>=2*c:
            ans=c*2*x
        else:
            ans=c*2*y+a*(x-y)
    elif x<y:
        if b>=2*c:
            ans=c*2*y
        else:
            ans=c*2*x+b*(y-x)
print(ans)