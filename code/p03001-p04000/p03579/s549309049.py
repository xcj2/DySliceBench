from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
import random
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
def ItoS(nn):
    return chr(nn+97)
def GI(V,E,Directed=False,index=0):
    org_inp=[]
    g=[[] for i in range(n)]
    for i in range(E):
        inp=LI()
        org_inp.append(inp)
        if index==0:
            inp[0]-=1
            inp[1]-=1
        if len(inp)==2:
            a,b=inp
            g[a].append(b)
            if not Directed:
                g[b].append(a)
        elif len(inp)==3:
            a,b,c=inp
            aa=(inp[0],inp[2])
            bb=(inp[1],inp[2])
            g[a].append(bb)
            if not Directed:
                g[b].append(aa)
    return g,org_inp
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
#sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()

def ran_input():
    import random
    n=random.randint(4,16)
    a=sorted([random.randint(0,5) for _ in range(n)])[::-1]
    return n,a

show_flg=False
show_flg=True

n,m=LI()
g,c=GI(n,m)

v=[-1 for i in range(n)]

def bfs(x):
    q=[x]
    v[x]=0
    while q:
        c=q.pop()
        for n in g[c]:
            if v[n]==-1:
                q.append(n)
                v[n]=1-v[c]

bfs(0)

flg=True
for i in range(n):
    MM=max([v[nb] for nb in g[i]])
    mm=min([v[nb] for nb in g[i]])
    if MM==mm and MM!=v[i]:
        continue
    else:
        flg=False
        break

#show(v,flg)
if flg:
    ans=sum(v)*(n-sum(v))-m
else:
    ans=n*(n-1)//2-m
print(ans)
