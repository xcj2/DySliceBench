def fac(n,k,p):
    ans=1
    for i in range(n-k+1,n+1):
        ans=(ans*i)%p
    return ans

def makeinv(length,p):
    L=[0,1]
    for i in range(2,length+1):
        x=p-((L[p%i]*(p//i))%p)
        L.append(x)
    return L

def comb(n,k,p):
    if k==0:
        return 1
    else:
        ans=fac(n,k,p)
        inv=makeinv(k,p)
        for i in range(1,k+1):
            ans=(ans*inv[i])%p
        return ans

N,K=map(int,input().split())
P=10**9+7

for i in range(1,K+1):
    x=comb(K-1,i-1,P)
    if N-K+1>=i:
        y=comb(N-K+1,i,P)
        print((x*y)%P)
    else:
        print(0)