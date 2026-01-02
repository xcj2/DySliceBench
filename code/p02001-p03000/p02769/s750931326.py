import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    n,k=map(int,input().split())
    
    def COMinit(n,MOD):
        fac,finv,inv=[0]*max(2,n+1),[0]*max(2,n+1),[0]*max(2,n+1)
        fac[0]=fac[1]=1
        finv[0]=finv[1]=1
        inv[1]=1
        for i in range(2,(n+1)):
            fac[i]=fac[i-1]*i%MOD
            inv[i]=MOD-inv[MOD%i]*(MOD//i)%MOD
            finv[i]=finv[i-1]*inv[i]%MOD
        return fac,finv,inv
    
    fac,finv,inv=COMinit(n,MOD)
    
    def COM(n, k, MOD):
        if n<k or n<0 or k<0:
            return 0
        return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD
    
    if k>=n:
        k=n-1
    ans=1
    for i in range(1,k+1):
        ans+=COM(n,i,MOD)*COM(n-1,i,MOD)
        ans%=MOD
    print(ans)
    

if __name__ == '__main__':
    main()
