from heapq import heappush,heappop,heapify
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
import math
import time
#import random
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

#sys.setrecursionlimit(10**5)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
#show_flg=True

n,c=LI()
s=[]

for i in range(n):
    x,v=LI()
    s.append((x,v))

show(c,s)
def solve(s):
    show('s',s)
    rt=-inf
    n=len(s)
    av=[0]
    for i in range(n):
        av.append(av[-1]+s[i][1])
    
    rav=[0]
    for i in range(n):
        rav.append(rav[-1]+s[-i-1][1])
    
    f=[-inf]*(n+1)
    for i in range(n):
        f[i+1]=max(av[i+1]-s[i][0],f[i])
    f.append(-inf)
    
    for i in range(1,n+1):
        rt=max(rt,rav[i]-(c-s[-i][0]),rav[i]-(c-s[-i][0])*2+f[n-i])

    return rt

ans=solve(s)
ans=max(ans,solve([(c-x,v) for x,v in s[::-1]]),0)
print(ans)




