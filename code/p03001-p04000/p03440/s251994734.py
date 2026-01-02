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
show_flg=True


n,m=LI()
a=LI()
g=[[] for _ in range(n)]
ans=0
cmp=0
for i in range(m):
    x,y=LI()
    g[x].append(y)
    g[y].append(x)

rest=[]
q=[]
v=[-1]*n

for i in range(n):
    if v[i]!=-1:
        continue
    p=[]
    cost=[]
    p.append(i)
    heappush(cost,a[i])
    while p:
        c=p.pop()
        v[c]=a[c]
        for nb in g[c]:
            if v[nb]==-1:
                p.append(nb)
                v[nb]=a[nb]
                heappush(cost,a[nb])
    ans+=heappop(cost)
    cmp+=1
    while cost:
        heappush(rest,heappop(cost))

if cmp==1:
    ans=0
elif len(rest)<cmp-2:
    ans="Impossible"
else:# cmp=n-m, n-m-1 edges needed, 2n-2m-2 vers, 2n-2m-2-cmp=n-m-2=cmp-2
    for i in range(cmp-2):
        ans+=heappop(rest)

print(ans)
