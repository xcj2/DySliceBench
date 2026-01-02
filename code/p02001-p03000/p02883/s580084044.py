import time
st_time=time.time()

from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import random
def I():
    return int(input())
def MI():
    return map(int,input().split())
def LI():
    return [int(i) for i in input().split()]
def LI_():
    return [int(i)-1 for i in input().split()]
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
ts=time.time()
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
show_flg=False
#show_flg=True

ans=0
n,k=LI()
a=LI()
f=LI()

a=sorted(a)[::-1]
f=sorted(f)
p=[a[i]*f[i] for i in range(n)]
show(a)
show(f)
show(p)

def check(z):
    c=0
    for i in range(n):
        c+=max(0,a[i]-z//f[i])
    if c<=k:
        rt=True
    else:
        rt=False
    return rt

ng=-1
ok=10**12

while ok-ng>1:
    mid=(ok+ng)//2
    fl=check(mid)
    if fl:
        ok=mid
    else:
        ng=mid
    show(ok,ng,fl)

ans=ok
print(ans)
