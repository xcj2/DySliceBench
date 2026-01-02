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

n=I()
a=LI()
b=LI()
c=LI()
ans=sum(b)

for i in range(1,n):
    if a[i]-a[i-1]==1:
        ans+=c[a[i]-1-1]
    
    
print(ans)
