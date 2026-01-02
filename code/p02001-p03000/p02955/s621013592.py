from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
#import random  # randome is not available at Codeforces
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def StoI():
    return [ord(i)-97 for i in input()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
#ts=time.time()
#sys.setrecursionlimit(10**6)
input=lambda: sys.stdin.readline().rstrip()
import sys
sys.setrecursionlimit(10**7)

show_flg=False
#show_flg=True
def devisors(x):
    rt=[1,x]
    for i in range(2,int(x**0.5+1)):
        if x%i==0:
            rt.append(i)
            if x//i!=i:rt.append(x//i)
    return rt
    
n,k=MI()
a=LI()
A=sum(a)
ds=devisors(A)
ans=1

for d in ds:
    r=[j%d for j in a]
    show(r,d)
    if sum(r)%d!=0:
        continue
    r.sort()
    ac=[0]
    for j in range(n):
        ac.append(ac[-1]+r[j])
    for j in range(1,n):
        if ac[j]==(n-j)*d-(ac[n]-ac[j]) and ac[j]<=k:
            ans=max(d,ans)
            show(j,d,ans)

print(ans)
show(ds)
    
