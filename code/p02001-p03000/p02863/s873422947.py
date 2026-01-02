def main():
    import sys
    def LI():
        return list(map(int, sys.stdin.readline().rstrip().split()))  # 空白あり

    def S():
        return sys.stdin.readline().rstrip()

    N, T = map(int, S().split())
    A = [0]
    B = [0]
    for i in range(N):
        a, b = LI()
        A.append(a)
        B.append(b)

    dp1 = [[0] * (T + 1) for i in range(N + 1)]
    # dp1[i][j] = 1~i番目から選んでT分以内に食べるときの美味しさの和の最大値
    dp2 = [[0] * (T + 1) for i in range(N + 2)]
    # dp2[i][j] = i~N番目から選んでT分以内に食べるときの美味しさの和の最大値

    for i in range(1, N + 1):
        for j in range(T + 1):
            if j >= A[i]:
                dp1[i][j] = max(dp1[i - 1][j], dp1[i - 1][j - A[i]] + B[i])
            else:
                dp1[i][j] = dp1[i - 1][j]
    for i in range(N, 0, -1):
        for j in range(T + 1):
            if j >= A[i]:
                dp2[i][j] = max(dp2[i + 1][j], dp2[i + 1][j - A[i]] + B[i])
            else:
                dp2[i][j] = dp2[i + 1][j]

    ans = dp1[N][T]
    for i in range(1, N + 1):  # 最後にi番目の料理を食べる
        for j in range(T):
            ans = max(ans, dp1[i - 1][j] + dp2[i + 1][T - 1 - j] + B[i])

    print(ans)

if __name__ == '__main__':
    main()