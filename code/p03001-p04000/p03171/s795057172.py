def solve():
    def max2(x, y): return x if x >= y else y
    def min2(x, y): return x if x <= y else y

    N = int(input())
    As = list(map(int, input().split()))

    if N%2 == 1:
        dp = [A for A in As]
    else:
        dp = [-A for A in As]

    for W in range(2, N+1):
        dp2 = [0] * (N-W+1)
        if (N-W)%2 == 0:
            for L in range(N-W+1):
                R = L+W-1
                dp2[L] = max2(As[L]+dp[L+1], As[R]+dp[L])
        else:
            for L in range(N-W+1):
                R = L+W-1
                dp2[L] = min2(-As[L]+dp[L+1], -As[R]+dp[L])
        dp = dp2

    print(dp[0])


solve()
