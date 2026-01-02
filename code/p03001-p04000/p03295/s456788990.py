from heapq import heappush, heappop
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
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
ts=time.time()
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
show_flg=False
#show_flg=True

ans=0
n,m=MI()
ed=[-1]*n
bg=[[] for _ in range(n)]
A=[0]*n
B=[0]*n
r=[]
for i in range(m):
    a,b=LI_()
    r+=[(a,b)]
    bg[a].append(b)
    ed[a]=b
    A[a]+=1
    B[b]+=1

show(r,A,B)
q=[]
for i in range(n):
    show(i,'q=',q,ans,end=' | ')
    if B[i]>0:
        ans+=1
        for j in q:
            B[j]-=1
        q=[]
    if A[i]>0:
        q+=bg[i]
    show(i,'q=',q,'ans=',ans,'A,B=',A,B)    
print(ans)