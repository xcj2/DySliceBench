N,M=map(int,input().split())
mod=10**9+7
Fact=[0 for i in range(M+1)]
Finv=[0 for i in range(M+1)]
Fact[0]=1
def inv(x):
    return pow(x,mod-2,mod)
for i in range(M):
    Fact[i+1]=Fact[i]*(i+1)
    Fact[i+1]%=mod
Finv[M]=inv(Fact[M])
for i in range(M-1,-1,-1):
    Finv[i]=(i+1)*Finv[i+1]
    Finv[i]%=mod
def P(n,k):
    return (Fact[n]*Finv[n-k])%mod
def C(n,k):
    return (Fact[n]*Finv[n-k]*Finv[k])%mod
ans=0
for k in range(N+1):
    if k%2==0:
        ans+=C(N,k)*P(M-k,N-k)
    else:
        ans-=C(N,k)*P(M-k,N-k)
    ans%=mod
print((ans*P(M,N))%mod)