#!/usr/bin/env pypy3
import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    a=[[0]*N for _ in range(N)]
    for i in range(N):
        a[i]=LI()
    MS=pow(2,N)
    
    dp=[0]*MS
    #状態Sの時の最大値
    #各Sから見て，全てのSの補集合Tを考える（bit1つだけ落とすのではなく，全部みる．例えば，1111から1100と0011とかもみる．）
    #Sの補集合Tで回して，dp[S]=max(dp[T]+dp[S-T])
    #Sに出てくるものが全て同じグループに入るパターンだけ別に計算する必要あり．
    
    #初期化，全部同じグループの場合を先に入れておく
    for S in range(1,MS):
        for j in range(N):
            if S>>j&1:#j番目のbitがあるなら，
                dp[S]=dp[S-(1<<j)]#j番目を加えた時の繊維を見てみる
                for k in range(N):
                    if S>>k&1:#k番目があれば
                        dp[S]+=a[j][k]
                break
            
    #メイン
    for S in range(1,MS):
        #Sの補集合，Tを列挙する
        T=S
        while T:
            T=(T-1)&S#bit演算を上手く使った補集合の列挙
            dp[S]=max(dp[S],dp[T]+dp[S-T])
            
    print(dp[MS-1])
                        
    
main()
