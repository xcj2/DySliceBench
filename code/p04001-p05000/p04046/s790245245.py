def mod_inv(inv,a,m):
    i=a
    if inv.get(a,0)!=0:
        return inv[a]
    e=m-2
    tmp=1
    while e!=1:
        if e%2==1:
            tmp*=a
            tmp%=m
        a*=a
        a%=m
        e//=2
    a*=tmp
    a%=m
    inv[i]=a
    return a

def factrial(fact,a,m):
    for i in range(1,a+1):
        fact[i]=fact[i-1]*i%mod

def comb(fact,inv,a,b,m):
    return (fact[a+b]*mod_inv(inv,fact[a],m)*mod_inv(inv,fact[b],m))%m

H,W,A,B=list(map(int,input().split()))
mod=10**9+7
fact=[1 for _ in range(H+W+1)]
inv={}
factrial(fact,H+W,mod)

ans=0
for i in range(W-B):
    ans+=comb(fact,inv,B+i,H-A-1,mod)*comb(fact,inv,W-B-1-i,A-1,mod)
    ans%=mod
print(ans)