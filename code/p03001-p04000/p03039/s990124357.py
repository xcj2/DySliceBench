# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    N,M,K=map(int,input().split())
    
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
    
    fac,finv,inv=COMinit(N*M,MOD)
    
    def COM(n, k, MOD):
        if n<k or n<0 or k<0:
            return 0
        return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD
    
    ans=0
    for a,b in [(N,M),(M,N)]:
        for i in range(1,a):
            ans+=(i*(a-i)*b**2)
            ans%=MOD
    ans*=COM(N*M-2,K-2,MOD)
    ans%=MOD
    print(ans)

if __name__ == '__main__':
    main()
