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

n,k=MI()
a=LI()

def slidmin(a,k):
    n=len(a)
    b=[0 for i in range(n-k+1)]
    q=deque()
    for i in range(k):
        while q and a[q[-1]]>=a[i]:
            q.pop()
        q.append(i)
    b[0]=a[q[0]]
    s=len(q)
    for i in range(k,n):
        while q and a[q[-1]]>=a[i]:
            q.pop()
            s-=1
        q.append(i)
        s+=1
        if q[0]<=i-k:
            q.popleft()
            s-=1
        b[i-k+1]=a[q[0]]
    return b

m=slidmin(a,k)
M=[-i for i in slidmin([-i for i in a],k)]
ans=1
p=-1
c=0
for i in range(k):
    if p<a[i]:
        c+=1
    else:
        c=1
    p=a[i]
fl=True if c==k else False

for i in range(n-k):
    if p<a[i+k]:
        c+=1
    else:
        c=1
    p=a[i+k]
    
    inc=1
    if c==k:
        if fl:
            inc=0
        fl=True
    if a[i]==m[i] and a[i+k]==M[i+1]:
        inc=0
    ans+=inc
print(ans)
