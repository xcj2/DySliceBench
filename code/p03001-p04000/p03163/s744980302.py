import sys
input = sys.stdin.readline
N,W = map(int,input().split())
wv = [list(map(int,input().split())) for i in range(N)]
f_min = 0 
dp = [[f_min] * (W+1) for _ in range(N+1)]
def chmin(a, b):
    if a > b:
        return b
    else:
        return a
def chmax(a,b):
    if a < b:
        return b
    else:
        return a
def main():
    # 初期条件

    for i in range(1,N+1):
        w,v = wv[i-1][0], wv[i-1][1]

        for sum_w in range(W+1):
            if sum_w - w >= 0:
                dp[i][sum_w] = chmax(dp[i][sum_w], dp[i-1][sum_w-w]+ v)
            
            dp[i][sum_w] = chmax(dp[i][sum_w],dp[i-1][sum_w])
    
    ans = 0
    for i in range(W+1):
        ans = chmax(ans,dp[N][i])
    print(ans)
            

            
 

if __name__ == "__main__":
    main()