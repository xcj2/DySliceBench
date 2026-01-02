import sys
input = sys.stdin.readline
N,W = map(int,input().split())
wv = [list(map(int,input().split())) for i in range(N)]
f_max = 10**9+100 

dp = [[f_max] * (10**5 +100) for _ in range(N+1)]
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
    dp[0][0]=0
    for i in range(1,N+1):
        w,v = wv[i-1][0], wv[i-1][1]
        for sum_v in range(10**5+1):
            if sum_v - v >= 0:
                dp[i][sum_v] = chmin(dp[i][sum_v], dp[i-1][sum_v-v]+ w)
            
            dp[i][sum_v] = chmin(dp[i][sum_v],dp[i-1][sum_v])
    
    ans = 0
    for i in range(10**5+100):
        if dp[N][i] <= W:
            ans = i
    
    print(ans)  

            
 

if __name__ == "__main__":
    main()