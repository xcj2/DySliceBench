N=int(input())
A=list(map(int,input().split()))
def prime_factorization(n):
    r={}
    for i in range(2,int(n**.5)+1):
        num=0
        while(True):
            x,y=divmod(n,i)
            if y!=0:
                break
            n=x
            num+=1
        if num>0:
            r[i]=num
    if n>1:
        r[n]=1
    return r
mod=10**9+7
def mul(a,b):
    return ((a%mod)*(b%mod))%mod
def div(a,b):
    return mul(a,pow(b,mod-2,mod))
from collections import defaultdict
d=defaultdict(int)
for a in A:
    r=prime_factorization(a)
    for k,v in r.items():
        d[k]=max(d[k],v)
X=1
for k,v in d.items():
    X=X*pow(k,v,mod)%mod
r=0
for a in A:
    r=(r+div(X,a))%mod
print(r)