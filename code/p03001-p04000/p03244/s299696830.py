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

n=I()
lis=LI()
ev,od=[],[]
for i in range(n):
    if i%2==0:
        ev.append(lis[i])
    else:
        od.append(lis[i])
c=Counter(ev)
d=Counter(od)
#print(c.most_common()[0][1])
#-c.most_common()[0]-d.most_common()[0]
if c.most_common()[0][0]==d.most_common()[0][0]:
    if c.most_common()[0][1]==n//2:
        ans=n//2
    elif c.most_common()[1][1]>=d.most_common()[1][1]:
        ans=len(od)-d.most_common()[0][1]+len(ev)-c.most_common()[1][1]
    elif c.most_common()[1][1]<d.most_common()[1][1]:
        ans=len(od)-c.most_common()[0][1]+len(ev)-d.most_common()[1][1]
else:
    ans=len(ev)+len(od)-c.most_common()[0][1]-d.most_common()[0][1]
print(ans)