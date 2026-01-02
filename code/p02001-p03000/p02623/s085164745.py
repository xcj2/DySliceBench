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

n,m,k=mp()
A=lmp()
B=lmp()
a=[A[0]]
b=[B[0]]
for i in range(1,n):
    a.append(a[i-1]+A[i])
for i in range(1,m):
    b.append(b[i-1]+B[i])
a.insert(0,0)
b.insert(0,0)
a.append(float("inf"))
b.append(float("inf"))
ans=0

ind=bisect.bisect_right(a,k)
j=0
ans=ind-1
for i in range(ind-1,-1,-1):
    while a[i]+b[j]>k or a[i]+b[j+1]<=k:
        j+=1
    ans=max(ans,i+j)
print(ans)