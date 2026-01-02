import math
import operator as op
from functools import reduce
from fractions import Fraction as frac

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom
def rd(p):
    if(p==0):
        return input()
    if(p==1):
        return int(input())
    if(p==2):
        return map(int,input().split())
    if(p==3):
        return list(map(int,input().split()))

global par
par=[-1 for i in range(100001)]
# t=rd(1)
def find(u):
    if(par[u]<0):
        return u
    else:
        return find(par[u])
def uni(x,y):
    u=find(x)
    v=find(y)
    if u==v:
        return
    if(par[u]<par[v]):
        par[u]+=par[v]
        par[v]=u
    else:    
        par[v]+=par[u]
        par[u]=v
t=1
for term in range(1,t+1):
    n,m=rd(2)
    for i in range(m):
        x,y,z=rd(2)
        uni(x,y)
        # print(par[1:n+1])
    ans=0
    for i in range(1,n+1):
        if(par[i]<0):
            ans+=1
    
    print(ans)
        
    
    