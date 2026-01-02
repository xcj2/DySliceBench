#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N,Z,W=MI()
    a=LI()
    inf=10**10
    
    #xがi枚目,yがj枚目を持っているとき
    dp=[[0]*(N+1) for _ in range(N+1)]
    
    #dpのj列目の,j行目より先の最大値を持っておく
    Mj=[0]*(N+1)
    
    #dpのi行目の,i列めより先の最小値を持っておく
    mi=[inf]*(N+1)
    
    #初期化
    dp[-1][0]=abs(a[-1]-W)
    Mj[0]=abs(a[-1]-W)
    for i in range(1,N):
        dp[i][-1]=abs(a[-1]-a[i-1])
        dp[-1][i]=abs(a[-1]-a[i-1])
        Mj[i]=abs(a[-1]-a[i-1])
        mi[i]=abs(a[-1]-a[i-1])
        
    for i in range(N-1,0,-1):
        for j in range(N-1,-1,-1):
            if i==j:
                continue
            if i>j:
                dp[i][j]=mi[i]
                Mj[j]=max(Mj[j],dp[i][j])
            else:
                dp[i][j]=Mj[j]
                mi[i]=min(mi[i],dp[i][j])
        
    print(Mj[0])
        

main()
