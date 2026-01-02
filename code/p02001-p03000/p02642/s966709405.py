import sys, math
#import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
#from bisect import bisect_left as bl, bisect_right as br, insort
#from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.buffer.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write(' '.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
#sys.setrecursionlimit(100000)
INF = float('inf')
mod = 998244353
#from decimal import Decimal

n=int(data())
A=mdata()
d=dd(int)
for i in range(n):
    d[A[i]]+=1
cnt=0
m=max(A)
P=[0]*(m+1)
for i in range(1,m+1):
    if d[i]>0:
        if P[i]==0:
            for j in range(2*i,m+1,i):
                P[j]=1
            if d[i]==1:
                cnt+=1
out(cnt)
