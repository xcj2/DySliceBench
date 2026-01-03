def main():
    from collections import Counter as ct
    fact=[1]
    mod=10**9+7
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(1,n+2):
        fact.append((fact[-1]*i)%mod)
    def inv_n(n,mod=10**9+7):return pow(n,mod-2,mod)
    def nCr(n,r,mod=10**9+7):return inv_n(fact[n-r]*fact[r]%mod,mod)*fact[n]%mod
    c=ct(a).most_common()[0][0]
    p,q=-1,-1
    for i in range(n+1):
        if a[i]==c:
            if p==-1:
                p=i
            else:
                q=i
    x=p+n-q
    for k in range(1,n+2):
        ans=0
        if k-2>=0:
            ans+=nCr(n-1,k-2)
        if k<=n-1:
            ans+=nCr(n-1,k)
        if k<=n:
            ans+=2*nCr(n-1,k-1)
        if k-1<=x:
            ans-=nCr(x,k-1)
        print((ans+mod)%mod)
main()