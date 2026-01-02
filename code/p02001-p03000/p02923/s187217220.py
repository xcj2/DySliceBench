from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
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
ans=0
c=0

for i in range(n-1):
    if a[i+1]<=a[i]:
        c+=1
    else:
        ans=max(ans,c)
        c=0
    
ans=max(ans,c)
print(ans)
