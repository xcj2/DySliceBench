import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write('\n'.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
from decimal import Decimal
from fractions import Fraction
#sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9)+7


n,k=mdata()
p=mdata()
c=mdata()
ans=-INF
for i in range(n):
    c1=[]
    a=i
    while True:
        a=p[a]-1
        c1.append(c[a])
        if a==i:
            break
    m1=0
    for j in range(min(k,len(c1))):
        m1+=c1[j]
        ans=max(m1,ans)
    if m1>0:
        t=k//len(c1)
        m1=max(0,m1*(t-1))
        ind=max(0,len(c1)*(t-1))
        ans=max(ans,m1)
        for i in range(ind,k):
            m1+=c1[i%len(c1)]
            ans=max(ans,m1)
out(ans)

