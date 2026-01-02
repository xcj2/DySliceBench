import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
#from bisect import bisect_left as bl, bisect_right as br, insort
#from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write('\n'.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
#from decimal import Decimal
#from fractions import Fraction
#sys.setrecursionlimit(100000)
#INF = float('inf')
mod = int(1e9)+7

n=int(data())
x=data()
c=x.count('1')
t1,t2=1,1
k1=0
k2=0
for i in range(n-1,-1,-1):
    if x[i]=='1':
        k1=(k1+t1)%(c+1)
        if c==1:
            continue
        k2=(k2+t2)%(c-1)
    t1=(t1*2)%(c+1)
    if c != 1:
        t2=(t2*2)%(c-1)
ans=[]
t1,t2=1,1
for i in range(n-1,-1,-1):
    if x[i]=='1':
        if c==1:
            ans.append(0)
            continue
        k=(k2-t2+c-1)%(c-1)
    else:
        k=(k1+t1)%(c+1)
    cnt=1
    while k:
        k=k%(bin(k)[2:].count('1'))
        cnt+=1
    ans.append(cnt)
    t1 = (t1 * 2) % (c + 1)
    if c!=1:
        t2 = (t2 * 2) % (c - 1)
outl(ans[::-1])
