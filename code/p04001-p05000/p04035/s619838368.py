from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
import math
import time
ts=time.time()
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
mo=10**9+7

n,l=MI()
a=LI()
ans='Impossible'
an=[]
for i in range(n-1):
    if a[i]+a[i+1]>=l:
        ans='Possible'
        an+=[i+1]
        break

print(ans)
if ans=='Possible':
    an+=list(range(an[0]+1,n))
    an+=list(range(1,an[0]))[::-1]
    for i in an[::-1]:
        print(i)