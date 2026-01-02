import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
a=lmp()
b=lmp()
sa=sum(a)
sb=sum(b)
l=[]
if sb>sa:
    print(-1)
    exit()
for i in range(n):
    l.append(-b[i]+a[i])
l=sorted(l,reverse=True)

r=[0]
s=0
ans=0
m=0
for i in range(n):
    if l[i]>0:
        s+=l[i]
        r.append(s)
    elif l[i]<0:
        ans+=1
        m+=l[i]
for i in range(len(r)):
    if m+r[i]>=0:
        print(ans+i)
        exit()