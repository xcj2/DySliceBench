# coding: utf-8

def array2d(d1, d2, init = None):
    return [[init for _ in range(d2)] for _ in range(d1)]


def solve(N, W, v, w):
    # dp[i][k]: 0~i?????????item????????????????????????k??\?????¨??????????????????????????´??????max value
    # return: dp[N-1][W]
    # dp[i][k] = max(dp[i-1][k], dp[i-1][k-w[i]] + v[i])
    # dp[i][0] = 0, dp[0][k] = 0(k<w[0]), v[0](otherwise)
    dp = array2d(N, W + 1)
    for k in range(0, W + 1):
        dp[0][k] = 0 if k < w[0] else v[0]
    for i in range(1, N):
        for k in range(0, W + 1):
            dp[i][k] = dp[i-1][k]
            if k - w[i] >= 0:
                dp[i][k] = max(dp[i][k], dp[i-1][k-w[i]] + v[i])
    return dp[N-1][W]



def main():
    N, W = map(int, input().split())
    v = [None] * N
    w = [None] * N
    for i in range(N):
        v[i], w[i] = map(int, input().split())
    print(solve(N, W, v, w))

main()