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
    p=[1]*(N+3)
    for i in range(N+2):
        p[i+1]=p[i]*2


    def make(L):
        #itertoolsのリストから整数を生成
        res=0
        for i in range(len(L)):
            res+=p[L[i]]
        return res

    import itertools
    
    for man in range(N):
        for ite in itertools.combinations(range(N),man):
            S=make(ite)
            if dp[S]==0:
                continue
            for i in range(N):
                if (S>>i)&1==0:#i桁目が立っていない
                    if a[man][i]==1:
                        dp[S+(1<<i)]+=dp[S]
                        dp[S+(1<<i)]%=mod
                        
        
    
    print(dp[-1])

                    
                    
    
        
    

main()
