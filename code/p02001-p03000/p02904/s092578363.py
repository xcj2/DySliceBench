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
na=[-i for i in a]
qs,ql=[],[]

def slidmin(a,k):
    n=len(a)
    b=[0 for i in range(n-k+1)]
    q=deque()
    for i in range(k):
        #show(q)
        while q and a[q[-1]]>=a[i]:
            q.pop()
        q.append(i)
    b[0]=a[q[0]]
    s=len(q)
    rt=[0 for _ in range(n-k+1)]
    if s==k:
        rt[0]=1
    for i in range(k,n):
        #show(q,i,a[q[0]])
        while q and a[q[-1]]>=a[i]:
            q.pop()
            s-=1
        q.append(i)
        s+=1
        if q[0]<=i-k:
            q.popleft()
            s-=1
        b[i-k+1]=a[q[0]]
    return rt,b

sz,m=slidmin(a,k)
sz,M=slidmin(na,k)
M=[-i for i in M]
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
show(a)
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
            show('c==k')
        fl=True
    if a[i]==m[i] and a[i+k]==M[i+1]:
        inc=0
        show('min=m,Max=M')
    show(i,inc)
    ans+=inc
print(ans)
