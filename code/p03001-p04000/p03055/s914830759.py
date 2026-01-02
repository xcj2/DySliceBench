from heapq import heappush, heappop
from collections import deque,defaultdict,Counter
import itertools
from itertools import permutations,combinations
import sys
import bisect
import string
#import math
#import time
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
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
#ts=time.time()
#sys.setrecursionlimit(10**6)
#input=sys.stdin.readline
show_flg=False
#show_flg=True

n=I()


g=[[] for i in range(1+n)]
v=[-1]*(1+n)

for i in range(n-1):
    a,b=LI_()
    g[a].append(b)
    g[b].append(a)

def dfs(cur,dep):
    mdep=0
    end=cur
    
    q=[]
    q.append((cur,dep))

    while q:
        cur,dep=q.pop()
        v[cur]=dep
        if dep>mdep:
            mdep=dep
            end=cur

        for nb in g[cur]:
            if v[nb]==-1:
                q.append((nb,dep+1))
    return mdep,end
    
dist,end=dfs(0,0)
v=[-1]*(1+n)
diam,beg=dfs(end,0)
show(end,beg,diam)
print(['First','Second'][diam%3==1])