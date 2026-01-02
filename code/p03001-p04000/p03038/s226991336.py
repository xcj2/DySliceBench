import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi
from operator import itemgetter
from copy import deepcopy
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [LI()for i in range(n)]
inf = 10**17
mod = 10**9 + 7

n,m=MI()
A=sorted(LI())
BC=[LI()for i in range(m)]
BC=sorted(BC,key=itemgetter(1),reverse=True)
#print(BC)
dif=[]
l=0
for i in range(m):
    dif+=[BC[i][1]]*BC[i][0]
    l+=BC[i][0]
    if l>=n:
        break
#print(dif)
for i in range(n):
    dif.append(0)
ans=0
for i in range(n):
    ans+=max(dif[i]-A[i],0)
print(ans+sum(A))