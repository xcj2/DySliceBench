#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,K=MI()
    a=[[]for _ in range(N)]
    for i in range(N):
        a[i]=LI()
        
    def matDot(A,B,MOD):
        N,M,L = len(A),len(A[0]),len(B[0])
        
        res = [[0]*L for i in range(N)]

        for i in range(N):
            for j in range(L):
                s = 0
                for k in range(M):
                    s = (s + A[i][k]*B[k][j]) % MOD
                res[i][j] = s
        
        return res

    def matPow(A,x,MOD):
        N = len(A)
        res = [[0]*N for i in range(N)]
        
        for i in range(N):
            res[i][i] = 1
        
        for i in range(x.bit_length()):
            if (x>>i) & 1:
                res = matDot(res,A,MOD)
            A = matDot(A,A,MOD)
    
        return res
    
    to=matPow(a,K,mod)
    ans=0
    for i in range(N):
        for j in range(N):
            ans=(ans+to[i][j])%mod
    print(ans)
    
        

main()
