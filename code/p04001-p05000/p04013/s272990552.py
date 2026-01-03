def main():
    N, A = map(int, input().split())
    *X, = map(int, input().split())

    ans = editorial_3d(N, A, X)
    # ans2 = editorial_2d(N, A, X)
    # assert ans == ans2
    if N <= 16:
        ans3 = part(N, A, X)
        assert ans == ans3

    print(ans)


def editorial_3d(N, A, X):
    """
    dp[N][N][sum]
    N枚の選択肢, N枚選ぶ, 合計値
    """
    max_sum = N * A
    dp = [[None] for _ in range(N+1)]
    for i in range(N+1):
        tmp = [[0] * (max_sum + 1) for _ in range(N+1)]
        dp[i] = tmp
    dp[0][0][0] = 1

    for i in range(1, N+1):
        for j in range(0, N+1):
            for k in range(max_sum + 1):
                v = dp[i-1][j][k]
                if k >= X[i-1] and j >= 1:
                    v += dp[i-1][j-1][k - X[i-1]]

                dp[i][j][k] = v

    ans = 0
    for j in range(1, N+1):
        if j * A <= max_sum:
            ans += dp[N][j][j * A]

    return ans


def editorial_2d(N, A, X):
    """TODO
    dp[N][sum]
    N枚の選択肢, 合計値
    """
    max_sum = N * A
    dp = [[0] * (2 * max_sum + 1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for k in range(max_sum, 2 * max_sum + 1):
            v = dp[i-1][k]
            if k >= X[i-1] - A:
                v += dp[i-1][k - X[i] - A]

            dp[i][k] = v

    ans = 0
    for j in range(1, N+1):
        ans += dp[j][0]

    return ans


def part(N, A, X):
    import sys
    sys.setrecursionlimit(10 ** 7)
    a = [0] * N

    def rec(i, n):
        ans = 0
        if i == n:
            s = 0
            c = 0
            # print(a)
            for j, b in enumerate(a):
                if b == 1:
                    s += X[j]
                    c += 1

            if c == 0:
                return 0
            if s / c == A:
                return 1
            else:
                return 0

        a[i] = 0
        ans += rec(i + 1, n)
        a[i] = 1
        ans += rec(i + 1, n)

        return ans

    ans = rec(0, N)
    return ans


if __name__ == '__main__':
    main()
