n,k=map(int,input().split())
r,s,p=map(int,input().split())
T=input()

def R(i):
    if T[i-1]==("s"):
        return r
    else:
        return 0
def S(i):
    if T[i-1]==("p"):
        return s
    else:
        return 0

def P(i):
    if T[i-1]==("r"):
        return p
    else:
        return 0

dp=[[0]*3 for _ in range(n+1)]
dp[0][0],dp[0][1],dp[0][2]=0,0,0
for i in range(1,k+1):
    dp[i][0]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])+R(i)
    dp[i][1]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])+S(i)
    dp[i][2]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])+P(i)
    

for i in range(0,n-k):
    if T[i]!="r":
        dp[i+k+1][2]=max(dp[i+k])+P(i+k+1)
    else:
        if dp[i+1][2]==0:
            dp[i+k+1][2]=max(dp[i+k])+P(i+k+1)
    if T[i]!="s":
        dp[i+k+1][0]=max(dp[i+k])+R(i+k+1)
    else:
        if dp[i+1][0]==0:
            dp[i+k+1][0]=max(dp[i+k])+R(i+k+1)

    if T[i]!="p":
        dp[i+k+1][1]=max(dp[i+k])+S(i+k+1)
    else:
        if dp[i+1][1]==0:
            dp[i+k+1][1]=max(dp[i+k])+S(i+k+1)

    
print(max(dp[n]))
