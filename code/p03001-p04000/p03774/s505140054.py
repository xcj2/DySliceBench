import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil
from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def printns(x): print('\n'.join(x))
def printni(x): print('\n'.join(list(map(str,x))))
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

n,m=MI()
stu=[]
che=[]
for i in range(n):
    stu.append(LI())
for j in range(m):
    che.append(LI())
for i in range(n):
    mini=inf
    num=0
    for j in range(m):
        l=abs(che[j][0]-stu[i][0])+abs(che[j][1]-stu[i][1])
        #print(l,end=" ")
        if l<mini:
            mini=l
            num=j+1
    print(num)