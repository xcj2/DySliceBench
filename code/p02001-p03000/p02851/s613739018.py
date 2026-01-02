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
def show(*inp,end='\n'):
    if show_flg:
        print(*inp,end=end)
YN=['Yes','No']
mo=10**9+7
inf=float('inf')
l_alp=string.ascii_lowercase
u_alp=string.ascii_uppercase
ts=time.time()
#sys.setrecursionlimit(10**6)
input=lambda: sys.stdin.readline().rstrip()

show_flg=False
#show_flg=True

n,k=LI()
a=LI()
b=[k-1]
for i in range(n):
    b.append((b[-1]+a[i])%k)
b=[(b[i]-i)%k for i in range(n+1)]
ans=0
dc=defaultdict(int)
show(a)
show(b)
for i in range(n+1):
    if i>=k:
        dc[b[i-k]]-=1
    ans+=dc[b[i]]
    #if dc[b[i]]>0:show(i,a[i],dc[b[i]],ans)
    #show(i,b[i],dc)
    dc[b[i]]+=1

print(ans)
