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
from copy import deepcopy
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
inf = 10**17
mod = 10**9 + 7
#s=input().rstrip()

n,m=MI()
ans=0
vote=[0 for i in range(m)]
likes=[]
for i in range(n):
    likes.append(LI())
#print(likes)
for j in range(len(likes)):
    for k in range(1,len(likes[j])):
        #print(likes[j][k])
        vote[likes[j][k]-1]+=1
#print(vote)
for v in vote:
    if v==n:
        ans+=1
print(ans)