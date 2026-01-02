import sys, math,os
from io import BytesIO, IOBase
#data = BytesIO(os.read(0,os.fstat(0).st_size)).readline
# from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
# from decimal import Decimal
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
#sys.setrecursionlimit(100000 + 1)
INF = 10**9
mod = 998244353


n=int(data())
a=mdata()
a.sort(reverse=True)
ans=a[0]
ind=1
k=0
for i in range(2,n):
   ans+=a[ind]
   k+=1
   if k==2:
       k=0
       ind+=1
out(ans)






