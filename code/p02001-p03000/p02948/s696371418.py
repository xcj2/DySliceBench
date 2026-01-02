import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
#from math import floor, ceil
#from operator import itemgetter
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [LI()for i in range(n)]
#inf = 10**17
#mod = 10**9 + 7

n,m=MI()
Q=[]
heapify(Q)
ar=[[] for i in range(m)]
for i in range(n):
    a,b=MI()
    if a<=m:
        ar[a-1].append(b)
#print(ar)
ans=0
for i in range(m):
    for j in ar[i]:
        heappush(Q,j*(-1))
    if Q:
        s=heappop(Q)*(-1)
        ans+=s
print(ans)