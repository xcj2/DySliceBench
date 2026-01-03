import time
ts=time.time()
from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
from itertools import permutations,groupby
import sys
import bisect
import string
import random
alp=string.ascii_lowercase
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]

n=I()
a=LI()
def solve(a,x):
    if a[0]*x>0:
        p=a[0]
        m=0
    else:
        p=x
        m=abs(a[0]-x)
    for i in range(1,n):
        t=-1 if p>0 else 1
        if (a[i]+p)*t>0:
            p+=a[i]
        else:
            m+=abs(a[i]+p-t)
            p+=a[i]+t*abs(a[i]+p-t)
    return m

print(min(solve(a,1),solve(a,-1)))