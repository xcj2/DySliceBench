import sys
input=sys.stdin.readline
def N(): return int(input())
def NM():return map(int,input().split())
def L():return list(NM())
def LN(n):return [N() for i in range(n)]
def LL(n):return [L() for i in range(n)]
from math import gcd
n=N()
mod=10**9+7
az=0
bz=0
zz=0
l=LL(n)
ans=1
import collections
d=collections.defaultdict(int)
for a,b in l:
    if a==0 and b==0:
        zz+=1
    elif a==0:
        az+=1
    elif b==0:
        bz+=1
    elif a<0 and b<0:
        a=-a
        b=-b
        x=gcd(a,b)
        d[(a//x,b//x)]+=1
    elif a<0:
        a=-a
        x=gcd(a,b)
        d[(-a//x,b//x)]+=1
    elif b<0:
        b=-b
        x=gcd(a,b)
        d[(-a//x,b//x)]+=1
    else:
        x=gcd(a,b)
        d[(a//x,b//x)]+=1
pow2=[1]*(n+1)
t=1
for i in range(1,n+1):
    t*=2
    t%=mod
    pow2[i]=t
ans*=(1+(pow2[az]-1)+(pow2[bz]-1))
for a,b in list(d.keys()):
    if a>0 and b>0:
        x=d[(a,b)]
        y=d[(-b,a)]
        ans*=(1+(pow2[x]-1)+(pow2[y]-1))
        ans%=mod
    else:
        if not (b,-a) in d:
            ans*=pow2[d[(a,b)]]
            ans%=mod
print((ans+zz-1)%mod)