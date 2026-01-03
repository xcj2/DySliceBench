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

w,h,n=MI()
rect=[0,w,0,h]
for i in range(n):
    a,b,c=MI()
    if c==1:
        rect[0]=max(a,rect[0])
    elif c==2:
        rect[1]=min(a,rect[1])
    elif c==3:
        rect[2]=max(b,rect[2])
    else:
        rect[3]=min(b,rect[3])
print(max(0,rect[3]-rect[2])*max(0,rect[1]-rect[0]))