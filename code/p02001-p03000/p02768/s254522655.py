#n=int(input())
n,a,b=map(int,input().split())
#l=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
mod=1000000007

#a!をmodで割ったあまりを求めるO(a)
def facmod(a,mod):
    res=1
    for i in range(1,a+1):
        res=(res*i)%mod
    return res

#a^nをmodでわったあまり 二分累乗法O(logn)
def modpow(a,n,mod):
    res=1
    while n>0:
        if n&1:
            res=(res*a)%mod
        a=(a*a)%mod
        n=n>>1
    return res

#フェルマーの小定理でaの逆元を求める
def modinv(a,mod):
    return modpow(a,mod-2,mod)

ans=(modpow(2,n,mod)-1)%mod

nca=1
ncb=1

#nCa
x=1;y=1
for i in range(n,n-a,-1):
    x=(i*x)%mod
y=facmod(a,mod)
yinv=modinv(y,mod)
nca=(x*yinv)%mod

#nCb
x=1;y=1
for i in range(n,n-b,-1):
    x=(i*x)%mod
y=facmod(b,mod)
yinv=modinv(y,mod)
ncb=(x*yinv)%mod

ans=(ans-nca-ncb)%mod

print(ans)