import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
#from bisect import bisect_left as bl, bisect_right as br, insort
#from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write(' '.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
from decimal import Decimal
#from fractions import Fraction
#sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9)+7


h,w,m=mdata()
bombh=[0]*h
bombw=[0]*w
s=set()
for i in range(m):
    x,y=mdata()
    x-=1
    y-=1
    s.add((x,y))
    bombh[x]+=1
    bombw[y]+=1
cnt=0
mh=max(bombh)
mw=max(bombw)
for (i,j) in s:
    if bombh[i]==mh and bombw[j]==mw:
        cnt+=1
k=0
for i in range(h):
    if bombh[i]==mh:
        k+=1
for i in range(w):
    if bombw[i]==mw:
        cnt-=k
if cnt==0:
    out(mh+mw-1)
else:
    out(mh+mw)