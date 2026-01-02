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

n,m,y=MI()
lis=[LI() for i in range(n)]
u=[]
point=[0 for i in range(m)]
for i in range(2**n):
    pay=0
    point=[0 for i in range(m)]
    for j in range(n):
        x=(i>>j) %2
        if x==1:
            for k in range(1,m+1):
                point[k-1]+=lis[j][k]
            pay+=lis[j][0]
    #print(min(point))
    if min(point)>=y:
        u.append(pay)
    #print(y)
if len(u)>0:
    print(min(u))
else:
    print("-1")