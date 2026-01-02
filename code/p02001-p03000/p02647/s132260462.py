import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
#from bisect import bisect_left as bl, bisect_right as br, insort
#from heapq import heapify, heappush, heappop
#from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write(' '.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
#sys.setrecursionlimit(100000)
INF = float('inf')
mod = 998244353
#from decimal import Decimal

n,k=mdata()
A=mdata()
for i in range(k):
    A1=[0]*(n+1)
    for j in range(n):
        A1[max(0,j-A[j])]+=1
        A1[min(n,j+A[j]+1)]-=1
    flag=True
    A[0]=A1[0]
    for j in range(1,n):
        A1[j]+=A1[j-1]
        A[j]=A1[j]
        if A1[j]!=n:
            flag=False
    if flag==True:
        break
print(*A)
