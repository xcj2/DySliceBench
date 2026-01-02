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
b=LI()
ans=0

for i in range(n-2):
    ans+=min(b[i+1],b[i])

ans+=b[0]
ans+=b[-1]
    
print(ans)
