import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,K=map(int,input().split())
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
    
    def COM(n, k, MOD):
        if n<k or n<0 or k<0:
            return 0
        fac,finv,inv=COMinit(n,MOD)
        return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD
    
    for i in range(K):
        print(COM(K-1,i,MOD)*COM(N-K+1,i+1,MOD)%MOD)

if __name__ == '__main__':
    main()
