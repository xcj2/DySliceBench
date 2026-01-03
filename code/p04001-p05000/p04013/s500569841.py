def main():
    N, A = map(int, input().split())
    *X, = map(int, input().split())

    ans = editorial_3d(N, A, X)
    ans2 = editorial_2d(N, A, X)
    assert ans == ans2
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
        tmp = [[0] * (2 * max_sum + 1) for _ in range(N+1)]
        dp[i] = tmp
    # 0枚選択肢のとき、合計0はあり得る
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
    """
    dp[N][sum]
    N枚の選択肢, 合計値
    """
    # X[i] がすべて0なら -A することで最低値になりうる
    # よって2倍確保して対応
    max_sum = 2 * (N * 50)
    dp = [[0] * (max_sum + 1) for _ in range(N+1)]
    # 真ん中の位置を0扱い
    dp[0][max_sum // 2] = 1

    for i in range(1, N+1):
        for k in range(max_sum + 1):
            v = dp[i-1][k]
            s = k - (X[i-1] - A)
            if 0 <= s <= max_sum:
                v += dp[i-1][s]

            dp[i][k] += v

    # 0枚のとき合計0はあり得るが、問題文より
    # これらのカードの中から 1枚以上を選び、
    # 選んだカードに書かれた整数の平均をちょうど Aにしたい
    # よって -1 しないといけない
    # 今回の組合せは、掛け算で増えないためそのまま減算で良い(はず)
    ans = dp[N][max_sum // 2] - 1

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
