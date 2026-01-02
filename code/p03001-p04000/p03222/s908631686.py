H,W,K=map(int,input().split())
if W==1:
    print(1)
    quit()

INF=1e9+7
dp=[[0]*W for i in range(H+1)]
dp[0][0]=1
d=W-1
a=max(0,d-1)
b=max(0,d-2)
f=max(0,d-3)
dic={0:0,1:1,2:2,3:4,4:7,5:12,6:20}
a=dic[a]+1
b=dic[b]+1
f=dic[f]+1
def func(w):
    c=dic[w-1]+1
    e=dic[d-w-1]+1
    return c*e
def func1(w):
    c=dic[w-1-1]+1
    e=dic[d-w-1]+1
    return c*e
def func2(w):
    c=dic[w-1]+1
    e=dic[d-w-1-1]+1
    return c*e
for i in range(H):
    for w in range(W):
        if w==0:
            dp[i+1][w]=(dp[i][w]*a)+(dp[i][w+1]*b)
            dp[i+1][w]%=INF
        elif w==W-1:
            dp[i+1][w]=(dp[i][w]*a)+(dp[i][w-1]*b)
            dp[i+1][w]%=INF
        elif w==1 :
            dp[i+1][w]=(dp[i][w]*b)+(dp[i][w-1]*b)+(dp[i][w+1]*f)
            dp[i+1][w]%=INF
        elif w==W-2:
            dp[i+1][w]=(dp[i][w]*b)+(dp[i][w-1]*f)+(dp[i][w+1]*b)
            dp[i+1][w]%=INF
        else:
            dp[i+1][w]=(dp[i][w]*func(w))+(dp[i][w-1]*func1(w))+(dp[i][w+1]*func2(w))
            dp[i+1][w]%=INF

print(int(dp[H][K-1]%INF))
