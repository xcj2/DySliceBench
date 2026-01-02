# coding: utf-8
import fractions 
import functools 

def pin(type=int):
    return map(type,input().split())

INF = float("inf")

def Flog_1(N,H):
    dp=[INF for i in range(N)]
    dp[0]=0  #h1=0
    dp[1]=abs(H[1]-H[0])
    for i in range(2,N):
        hop1=dp[i-1]+abs(H[i-1]-H[i]) 
        hop2=dp[i-2]+abs(H[i-2]-H[i]) 
        #print(hop1,hop2)
        dp[i]=hop1 if hop1<hop2 else hop2
    return dp
def Flog_1_Another(N,H):
    dp=[INF for i in range(N)]
    dp[0]=0  #h1=0
    for i in range(0,N):
        for k in [1,2]:
            if i+k <N:
                dp[i+k]=min(dp[i+k],dp[i]+abs(H[i+k]-H[i]))
    return dp

def Flog_2(N,K,H):
    dp=[INF for i in range(N)]
    dp[0]=0  #h1=0,default position
    for i in range(1,N):
        temp = INF
        for k in range(1,K+1):
            if i-k < 0:break
            else:
                temp = min(temp,(dp[i-k]+abs(H[i-k]-H[i])))
                
        dp[i]=temp
    return dp
def Flog_2_Another(N,K,H):
    dp=[INF for i in range(N)]
    dp[0]=0  #h1=0
    for i in range(0,N):
        for k in range(1,K+1):
            if i+k <N:
                dp[i+k]=min(dp[i+k],dp[i]+abs(H[i+k]-H[i]))
    return dp
def Flog_2_YETAnother(N,K,H):
    if N == 1:
        return 0
    else:
        map(min,[Flog_2_YETAnother(N-i,K,H) for i in range(1,N+1)])
 
def vacation(N):
   
    dp=[[0]*3 for i in range(N)]
    dp[0]=list(pin())
    for i in range(1,N):
       
        temp=list(pin())
       
        dp[i][0]= max(dp[i-1][1],dp[i-1][2])+temp[0]
        dp[i][1]= max(dp[i-1][2],dp[i-1][0])+temp[1]
        dp[i][2]= max(dp[i-1][0],dp[i-1][1])+temp[2]
        
    return max(dp[-1])

N,=pin()
 
#output
print(vacation(N))