#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    a=[[] for _ in range(N)]
    for i in range(N):
        a[i]=LI()
    
    #dp[S]は状態Sから何通りあるか？男性は1から順に，女性マッチング情報がS   
    M=pow(2,N) 
    dp=[0]*M
    dp[0]=1
    
    def bit_cnt(N):
        B=bin(N)
        return B.count("1")

    
    for S in range(M-1):
        if dp[S]==0:
            continue
        man=bit_cnt(S)
        for i in range(N):
            if (S>>i)&1==0:#i桁目が立っていない
                if a[man][i]==1:
                    dp[S+(1<<i)]+=dp[S]
                    dp[S+(1<<i)]%=mod
                        
        
    
    print(dp[-1])

                    
                    
    
        
    

main()
