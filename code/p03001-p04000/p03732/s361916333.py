import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

import bisect

def main():
    mod=10**9+7
    N,W=MI()
    w=[0]*N
    v=[0]*N
    for i in range(N):
        w[i],v[i]=MI()
    w1=w[0]
    for i in range(N):
        w[i]-=w1
        
    a=set([0])
    for i in range(N+1):
        for j in range(3*i+1):
            ww=w1*i+j
            if ww>W:
                break
            a.add(ww)
    a=list(a)
    a.sort()#sortしないと順番がぐちゃぐちゃになっている？かも
    M=len(a)
    
    
    #dp[i][j]はiまでの商品で,重さa[j]のときの価値の最大
    dp=[[-1]*(M) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0]=0
    ans=0
    
    for i in range(N):
        for j in range(M):
            if dp[i][j]!=-1:
                dp[i+1][j]=max(dp[i+1][j],dp[i][j])
                ww=a[j]+w1+w[i]
                if ww<=W:
                    jj=bisect.bisect_left(a,ww)
                    dp[i+1][jj]=max(dp[i+1][jj],dp[i][j]+v[i])
                    ans=max(ans,dp[i+1][jj])
                    
    print(ans)
                    
    
            

main()
