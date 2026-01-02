import sys
# input処理を高速化する
input = sys.stdin.readline

def chmax(a, b):
    if a >= b:
        return a
    return b

def chmin(a, b):
    if a <= b:
        return a
    return b

def main():
    N = int(input())
    a = list(map(int, input().split()))

    # aiからajのX−Yの最大値
    # [左端,右端)=[l,r)からの遷移    
    # 左をとる[l+1,r)、右をとる[l,r−1)の2通り
    dp = [[0] * (N+2)  for _ in range(N+2)]

    for len in range(1, N + 1):
        for i in range(N + 1 - len):
            j = i + len

            if (N - len) % 2 == 0:
                dp[i][j] = chmax(dp[i + 1][j] + a[i], dp[i][j - 1] + a[j - 1])
            else:
                dp[i][j] = chmin(dp[i + 1][j] - a[i], dp[i][j - 1] - a[j - 1])

    print(dp[0][N])

main()