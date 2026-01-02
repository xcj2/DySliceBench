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
    for i in range(0,N):
        for k in [1,2]:
            if i+k <N:
                dp[i+k]=min(dp[i+k],dp[i]+abs(H[i+k]-H[i]))
    return dp
"""
|# Flog1との違い:飛ぶ段数に（1個か2個という）制限がない
|    
"""    
def Flog_2(N,K,H):#pypy回答でなんとかおｋ
    dp=[INF for i in range(N)]#{DP table}:最小化問題なので初期値はINF, h1=H[0]）
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
def Flog_2_Another(N,K,H):#"配る"DP
    dp=[INF for i in range(N)]#{DP table}:最小化問題なので初期値はINF, h1=H[0]）
    dp[0]=0  #h1=0
    for i in range(0,N):
        for k in range(1,K+1):
            if i+k <N:
                dp[i+k]=min(dp[i+k],dp[i]+abs(H[i+k]-H[i]))
    return dp
def Flog_2_YETAnother(N,K,H):#python提出やりたい再帰関数やりたいよお
    #つまり、つまりf2Y(N,K,H)->f2Y((0 or enough value to be default),K,H)に持っていく関数を書くぞ
    if N == 1:
        return 0
    else:
        map(min,[Flog_2_YETAnother(N-i,K,H) for i in range(1,N+1)])
    #詰んだ

def vacation(N):
    #これは二次元で書けばいいですね？
    dp=[[0]*3 for i in range(N)]#[i]+1日目にある行動をした時にできる幸福度の最大値 
    dp[0]=list(pin())
    #print(dp[0])
    for i in range(1,N):
        #めんどいのでfor分かかない、ごめんね
        temp=list(pin())
       # print("*",temp)
        dp[i][0]= max(dp[i-1][1],dp[i-1][2])+temp[0]
        dp[i][1]= max(dp[i-1][2],dp[i-1][0])+temp[1]
        dp[i][2]= max(dp[i-1][0],dp[i-1][1])+temp[2]
        #print(dp[i])
    return max(dp[-1])
#input
N,=pin()

#output
print(vacation(N))