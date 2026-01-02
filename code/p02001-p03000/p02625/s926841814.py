n,m=map(int,input().split())

U=10**6
mod=10**9+7

fact=[1]*(U+1)
fact_inv=[1]*(U+1)

for i in range(1,U+1):
    fact[i]=(fact[i-1]*i)%mod
fact_inv[U]=pow(fact[U],mod-2,mod)

for i in range(U,0,-1):
	fact_inv[i-1]=(fact_inv[i]*i)%mod

def comb(n,k):
    if k<0 or k>n:
        return 0
    x=fact[n]
    x*=fact_inv[k]
    x%=mod
    x*=fact_inv[n-k]
    x%=mod
    return x
def div(a,b):
    return (a*pow(b,mod-2,mod))%mod

def p(n,k):
    return div(fact[n],fact[n-k])
ans=0
for i in range(n+1):
    t=(comb(n,i)*p(m-i,n-i))%mod
    if i%2:ans=(ans-t)%mod
    else:ans=(ans+t)%mod
ans=(ans*p(m,n))%mod
print(ans)