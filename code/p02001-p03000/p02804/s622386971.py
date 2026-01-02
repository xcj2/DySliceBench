import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
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
        return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD
    
    
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    
    fac,finv,inv=COMinit(N+K,MOD)
    sumcom=[0]*N
    sumcom[0]=1
    for i in range(N-1):
        sumcom[i+1]=sumcom[i]+COM(i+1+K-2,K-2,MOD)
    
    sum_min=0
    sum_max=0
    for i,x in enumerate(A):
        if i<=N-K:
            sum_min+=sumcom[(N-i)-K]*x
            sum_min%=MOD
        if i>=K-1:
            sum_max+=sumcom[i-(K-1)]*x
            sum_max%=MOD
    ans=sum_max-sum_min if sum_max-sum_min>=0 else sum_max-sum_min+MOD
    print(ans)
    

if __name__ == '__main__':
    main()
