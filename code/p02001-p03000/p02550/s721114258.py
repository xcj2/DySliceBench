import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
from decimal import Decimal
# from fractions import Fraction
# sys.setrecursionlimit(100000)
mod = 998244353
INF=float('inf')

n,x,m=mdata()
d=dd(int)
d[x]=0
l=[x]
ans=x
for i in range(n-1):
    x**=2
    if x%m in d:
        x%=m
        ans+=sum(l[d[x]:])*((n-1-i)//(len(l)-d[x])) + sum(l[d[x]:d[x]+((n-1-i)%(len(l)-d[x]))])
        break
    else:
        x%=m
        ans+=x
        d[x]=i+1
        l.append(x)
out(ans)