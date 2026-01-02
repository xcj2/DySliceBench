from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
import math
import time
ts=time.time()
sys.setrecursionlimit(10**6)
def SI():
    return input().split()
def MI():
    return map(int,input().split())
def I():
    return int(input())
def LI():
    return [int(i) for i in input().split()]
YN=['Yes','No']
mo=10**9+7

n=I()
t=[]
d=[]
nx=[0]*n
for i in range(n):
    a=[i-1 for i in LI()[::-1]]
    nx[i]=a.pop()
    t.append(a)
    d.append([-1]*(n))

flg=True
ans=0
MacthNum=0
yet=set(range(n))
n_yet=set(range(n))
while flg and MacthNum<n*(n-1)//2:
    elp=time.time()-ts
    if elp>1.8:
        ans=n*(n-1)//2
        break
    ans+=1
    IsMatch=False
    done=set()
    for i in yet:
        if (i in done) or (nx[i] in done) or nx[i]==n:
            continue
        c1=i
        c2=nx[i]
        if c1==nx[c2]:
            IsMatch=True
            MacthNum+=1
            if t[c1]:
                n_i=t[c1].pop()
            else:
                n_i=n
                n_yet.remove(c1)
            if t[c2]:
                n_n_i=t[c2].pop()
            else:
                n_n_i=n
                n_yet.remove(c2)
            nx[nx[i]],nx[i]=n_n_i,n_i
            done.add(c1)
            done.add(c2)
    yet=[i for i in n_yet]
    ans=ans if IsMatch else -1
    flg=True if IsMatch else False

print(ans)
