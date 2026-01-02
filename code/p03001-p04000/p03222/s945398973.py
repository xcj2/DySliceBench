high,wide,end=map(int,input().split())

dp=[[[-1,-1,-1] for _ in range(wide)] for _ in range(high)]
fb=[-1 for _ in range(8)]
fb[0]=1
fb[1]=1
def MakeFibo(i):
    if fb[i-1]==-1:
        fb[i-1]=MakeFibo(i-1)
    if fb[i-2]==-1:
        fb[i-2]=MakeFibo(i-2)
    fb[i]=fb[i-1]+fb[i-2]
    return fb[i]
MakeFibo(7)
#fit 0
wide-=1
high-=1
end-=1
mod=10**9+7
def NZ(x):  #NegativeZero
    if x<0:
        return 0
    else:
        return x


def amida(h,w,f):
    dp[h][w][2]=fb[NZ(w)]*fb[NZ(wide-w)]
    if f == 1: #go straight
        if h==high and w==end:
            dp[h][w][f]=1
        elif h==high:
            dp[h][w][f]=0
        else: #sum under
            if dp[h+1][w][1] == -1:
                amida(h+1,w,1)
            if dp[h+1][w][0] == -1:
                amida(h+1,w,0)
            dp[h][w][f]=dp[h+1][w][0]+dp[h+1][w][1]*dp[h+1][w][2]
    else: #f==0 go side
        dp[h][w][f]=0
        if w-1>=0: #sum left
            if dp[h][w-1][1]==-1:
                amida(h,w-1,1)
            dp[h][w][f]+=dp[h][w-1][1]*fb[NZ(w-1)]*fb[NZ(wide-w)]
        if w+1<=wide: #sum right
            if dp[h][w+1][1]==-1:
                amida(h,w+1,1)
            dp[h][w][f]+=dp[h][w+1][1]*fb[NZ(w)]*fb[NZ(wide-w-1)]
    dp[h][w][f]%=mod

amida(0,0,0)
amida(0,0,1)

print((dp[0][0][0]+dp[0][0][1]*dp[0][0][2])%mod)