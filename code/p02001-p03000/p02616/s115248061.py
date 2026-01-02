import sys, math,os
from io import BytesIO, IOBase
#data = BytesIO(os.read(0,os.fstat(0).st_size)).readline
# from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
from decimal import Decimal
from fractions import Fraction
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
#sys.setrecursionlimit(100000 + 1)
INF = 10**9
mod = 10**9 + 7


n,k=mdata()
a=mdata()
n1,p=-1,-1
a1=[(abs(a[i]),a[i]) for i in range(n)]
a1.sort(reverse=True)
ans=1
c=1
for i in range(k):
    if a1[i][1]>0:
        p=i
    elif a1[i][1]<0:
        n1=i
        c*=-1
    else:
        c=0
    ans=(ans*a1[i][1])%mod
if c>=0:
    out(ans%mod)
else:
    b1=0
    b2=0
    for i in range(k,n):
        if a1[i][1]>=0 and b1==0:
            u1,v1=a1[n1][1],a1[i][1]
            b1=1
            c=1
        if a1[i][1]<0 and p!=-1 and b2==0:
            u2,v2=a1[p][1],a1[i][1]
            b2=1
            c=1
    if c<0:
        ans=1
        for i in range(k):
            ans = (ans*a1[n-i-1][1])%mod
    else:
        if b1==1 and b2==1:
            if Fraction(v1,u1)<Fraction(v2,u2):
                ans=ans*pow(u1,mod-2,mod)*v1
            else:
                ans = ans * pow(u2, mod - 2, mod) * v2
        elif b1==1:
            ans = ans * pow(u1, mod - 2, mod) * v1
        else:
            ans = ans * pow(u2, mod - 2, mod) * v2
    out(ans%mod)







