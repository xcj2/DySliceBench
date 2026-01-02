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

n=I()
ans=0
c=[[] for i in range(n)]
for i in range(n):
    a=I()
    for j in range(a):
        x,y=LI()
        x-=1
        c[i].append((x,y))

for bit in range(2**n):
    t=[1 if (bit>>i)&1 else 0 for i in range(n)]
    flg=True    
    for i in range(n):
        if t[i]==1:
            for x,y in c[i]:
                if t[x]!=y:
                    flg=False
    if flg:
        ans=max(ans,sum(t))
    
print(ans)
