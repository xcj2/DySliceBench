import bisect,collections,copy,itertools,math,string
def I(): return int(input())
def S(): return input()
def LI(): return list(map(int,input().split()))
def LS(): return list(input().split())
##################################################
H,W = LI()
S = [S() for _ in range(H)]
dp = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        judge = 1 if S[i][j]=='#' else 0
        if i==0: #0行目
            if j==0:
                dp[0][0] = judge
            else:
                dp[0][j] = dp[0][j-1]+judge*(0 if S[0][j-1]=='#' else 1)
        else: #0行目以外
            if j==0:
                dp[i][0] = dp[i-1][0]+judge*(0 if S[i-1][j]=='#' else 1)
            else:
                temp1 = dp[i][j-1]+judge*(0 if S[i][j-1]=='#' else 1)
                temp2 = dp[i-1][j]+judge*(0 if S[i-1][j]=='#' else 1)
                dp[i][j] = min(temp1,temp2)
print(dp[-1][-1])
