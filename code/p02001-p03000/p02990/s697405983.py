def n_func(n,mod=10**9+7):
    ans=1
    for i in range(1,n+1):
        ans=(ans*i)%mod
    return ans
def inv_n(n,mod=10**9+7):
    return pow(n,mod-2,mod)
def nPr(n,r,mod=10**9+7):
    ans=n_func(n-r,mod)
    ans=inv_n(ans,mod)
    return ans*n_func(n,mod)%mod
def nCr(n,r,mod=10**9+7):
    ans=n_func(n-r,mod)*n_func(r,mod)%mod
    ans=inv_n(ans,mod)
    return ans*n_func(n,mod)%mod

N,K=map(int,input().split())

mod=10**9+7
for i in range(1,K+1):
    if N-K+1<i or K-1<i-1:
        print(0)
    else:
        print((nCr(N-K+1,i)*nCr(K-1,i-1))%mod)
