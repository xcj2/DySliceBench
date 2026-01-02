# coding: utf-8
#便利そうなので置いとく
import fractions 
import functools 
#再帰関数を使うときは、再帰上限を上げておこうね！
import sys
sys.setrecursionlimit(200000000)
# my functions here!
def pin(type=int):
    return map(type,input().split())
"""
------------------------------------------------------------------
|OBJECTIVE:                                                      |
|Educatinal DP contest("https://atcoder.jp/contests/dp")を解こう!|
------------------------------------------------------------------
"""
#solution:
INF = float("inf")
"""
|#遷移式を考える
|   つまり、漸化式みたいに i回目までの結果を保存して、i+1回目の評価を行う
"""
def Flog_1(N,H):
    dp=[INF for i in range(N)]#{DP table}:最小化問題なので初期値はINF, h1=H[0]）
    dp[0]=0  #h1=0
    dp[1]=abs(H[1]-H[0])#ほら、"2段前"がないから…
    for i in range(2,N):
        hop1=dp[i-1]+abs(H[i-1]-H[i]) 
        hop2=dp[i-2]+abs(H[i-2]-H[i]) 
        #print(hop1,hop2)
        dp[i]=hop1 if hop1<hop2 else hop2
    return dp
def Flog_1_Another(N,H):#"配る"DP
    dp=[INF for i in range(N)]#{DP table}:最小化問題なので初期値はINF, h1=H[0]）
    dp[0]=0  #h1=0
    for i in range(1,N-1):
        pass
    
def Flog_2(N,K,H):
    dp=[INF for i in range(N)]#{DP table}:最小化問題なので初期値はINF, h1=H[0]）
    """
    |# Flog1との違い:飛ぶ段数に（1個か2個という）制限がない
    |    
    """
    dp[0]=0  #h1=0,default position
    for i in range(1,N):#k段前から飛んでくることを考えよ
        temp = INF
        for k in range(1,K+1):
            if i-k < 0:break
            else:
                #print("*",i-k)
                temp = min(temp,(dp[i-k]+abs(H[i-k]-H[i])))
                
        dp[i]=temp
        #print("*",dp)
    return dp
#input
N,K=pin()
H =list(pin())

#output
print(Flog_2(N,K,H)[-1])