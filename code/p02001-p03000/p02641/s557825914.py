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

x,n=mdata()
p=set(mdata())
m=x
v=0
for i in range(1,102):
    if i not in p:
        if abs(i-x)<m:
            v=i
            m=abs(i-x)
out(v)

