def solve():
    def max2(x, y): return x if x >= y else y
    def min2(x, y): return x if x <= y else y

    N = int(input())
    As = list(map(int, input().split()))

    dp = [[0]*(N) for _ in range(N)]

    if N%2 == 1:
        for i, A in enumerate(As):
            dp[i][i] = A
    else:
        for i, A in enumerate(As):
            dp[i][i] = -A

    for W in range(2, N+1):
        if (N-W)%2 == 0:
            for L in range(N-W+1):
                R = L+W-1
                dp[L][R] = max2(As[L]+dp[L+1][R], As[R]+dp[L][R-1])
        else:
            for L in range(N-W+1):
                R = L+W-1
                dp[L][R] = min2(-As[L]+dp[L+1][R], -As[R]+dp[L][R-1])

    print(dp[0][N-1])


solve()
