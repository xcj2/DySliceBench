import sys
input = sys.stdin.readline
n = int(input())
abc = [list(map(int,input().split())) for i in range(n)]
f_min = 0 
dp = [[f_min] * 3 for _ in range(n)]
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
    dp[0][0], dp[0][1], dp[0][2] = abc[0][0], abc[0][1], abc[0][2]
    for i in range(1,n):
            a,b,c = abc[i][0], abc[i][1], abc[i][2]
            dp[i][0] = chmax(dp[i][0], chmax(dp[i-1][1] + a, dp[i-1][2] +a))
            dp[i][1] = chmax(dp[i][1], chmax(dp[i-1][0] + b, dp[i-1][2] +b))
            dp[i][2] = chmax(dp[i][2], chmax(dp[i-1][0] + c, dp[i-1][1] +c))
    print(chmax(dp[n-1][0], chmax(dp[n-1][1],dp[n-1][2])))

if __name__ == "__main__":
    main()