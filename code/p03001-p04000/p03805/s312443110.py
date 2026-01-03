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
input=sys.stdin.readline
show_flg=False
#show_flg=True

n,m=MI()
g=[[] for _ in range(n)]
t=1<<n
mask=t-1
for i in range(m):
    a,b=LI_()
    g[a].append(b)
    g[b].append(a)

dp=[[0]*n for _ in range(t)]
dp[1][0]=1

for s in range(t):
    for h in range(n):
        if s&(1<<h)==0:
            #show('pas1')
            continue
        for f in g[h]:
            if s&(1<<f)==0:
                #show('pas2')
                continue
            
            dp[s][h]+=dp[s-(1<<h)][f]
            show('!dp','s,h,f',bin(s+t)[3:],h,f,'|',dp[s][h],dp[s-(1<<h)][f])

ans=0
for i in range(1,n):
    ans+=dp[t-1][i]

print(ans)
show(g)
show(dp)
