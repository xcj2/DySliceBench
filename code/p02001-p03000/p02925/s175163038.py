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
nx=[-1]*n
for i in range(n):
    a=[i-1 for i in LI()[::-1]]
    nx[i]=a.pop()
    t.append(a)

IsMatch=True
ans=0
MacthNum=0
search=set(range(n))

while IsMatch and MacthNum<n*(n-1)//2:
    ans+=1
    IsMatch=False
    done=set()
    nx_search=[]
    for i in search:
        if (i in done) or (nx[i] in done) or nx[i]==-1:
            continue
        c1=i
        c2=nx[i]
        if c1==nx[c2]:
            IsMatch=True
            MacthNum+=1
            if t[c1]:
                n_i=t[c1].pop()
                nx_search.append(c1)
            else:
                n_i=-1
            if t[c2]:
                n_n_i=t[c2].pop()
                nx_search.append(c2)
            else:
                n_n_i=-1
            nx[nx[i]],nx[i]=n_n_i,n_i
            done.add(c1)
            done.add(c2)
    search=[i for i in nx_search]
    ans=ans if IsMatch else -1

print(ans)