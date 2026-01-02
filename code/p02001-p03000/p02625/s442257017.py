def main():
    mod=1000000007
    inv=lambda x: pow(x,mod-2,mod)
    n,m=map(int,input().split())
    
    Fact=[1]
    for i in range(1,m+1):
        Fact.append(Fact[i-1]*i%mod)
    Finv=[0]*(m+1)
    Finv[-1]=inv(Fact[-1])
    for i in range(m-1,-1,-1):
        Finv[i]=Finv[i+1]*(i+1)%mod
    def comb(n,r):
        if n<r:
            return 0
        return Fact[n]*Finv[r]*Finv[n-r]%mod
    def perm(n,r):
        if n<r:
            return 0
        return Fact[n]*Finv[n-r]%mod
    
    ans=0
    p=1
    for i in range(n+1):
        ans+=comb(n,i)*perm(m,i)*perm(m-i,n-i)**2*p
        ans%=mod
        p*=-1
    print(ans)
    
if __name__=='__main__':
    main()