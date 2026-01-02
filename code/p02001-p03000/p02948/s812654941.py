from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
YNeos='YNeos'
mo=10**9+7
imp='IMPOSSIBLE'

n,m=MI()
w=[[] for _ in range(10**5+3)]
for i in range(n):
    a,b=MI()
    w[a].append(-b)

q=[]
ans=0
for i in range(1,m+1):
    for j in w[i]:
        heappush(q,j)
    if q:
        x=heappop(q)
        ans+=-x
        

print(ans)
