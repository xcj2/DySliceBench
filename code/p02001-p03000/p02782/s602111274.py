def main():
    mod=1000000007
    r1,c1,r2,c2=map(int,input().split())
    Fact=[1] #階乗
    n=r2+c2+1
    for i in range(1,n+1):
        Fact.append(Fact[i-1]*i%mod)
    Finv=[0]*(n+1) #階乗の逆元
    Finv[-1]=pow(Fact[-1],mod-2,mod)
    for i in range(n-1,-1,-1):
        Finv[i]=Finv[i+1]*(i+1)%mod
    def comb(n,r):
        if n<r:
            return 0
        return Fact[n]*Finv[r]*Finv[n-r]%mod
    def f(r,c):
        ret=0
        for i in range(r+1):
            ret+=comb(c+i+1,c)
            ret%=mod
        return ret
 
    print((f(r2,c2)-f(r2,c1-1)-f(c2,r1-1)+f(r1-1,c1-1))%mod)
    
if __name__=='__main__':
    main()