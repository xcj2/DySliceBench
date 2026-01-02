from heapq import heappush, heappop
from collections import deque
import itertools
from itertools import permutations
import sys
import bisect
sys.setrecursionlimit(10**6)
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
YN=['YES','NO']
YNeos='YNeos'
mo=10**9+7
imp='IMPOSSIBLE'


n=I()
a=LI()
ans=1
c=[i for i in a]
c.sort()
def rp(i,j):
    b=[i for i in a]
    b[i],b[j]=b[j],b[i]
    return b
for i in range(n):
    for j in range(i,n):
        d=rp(i,j)
        if d==c:
            ans=0

print(YN[ans])

