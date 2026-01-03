def read_input():
    n, a = map(int, input().split())
    xlist = list(map(int, input().split()))
    return n, a, xlist


def make_matrix():
    dp = [
        [
            [0] * ((n + 1) * max(max(xlist), a)) for _ in range(n + 1)
        ] for _ in range(n + 1)
    ]



def submit():
    n, a, xlist = read_input()

    dp = [
        [
            [0] * ((n + 1) * max(max(xlist), a)) for _ in range(n + 1)
        ] for _ in range(n + 1)
    ]

#   dp[j][k][s] : j枚目までのカードでk枚選び、合計sにする方法の数
#         (1) dp[0][0][0] : 1枚も選ばずに合計0にする方法は1種類
#               j = k = s = 0のとき
#         (2) dp[j][k][s] = dp[j - 1][k][s] if xj > s : j枚目のカードがsより大きいとき、sを作りようがないのでj-1枚目までの手法と一緒
#               j > 0, xj > sのとき
#         (3) dp[j][k][s] = dp[j - 1][k][s] + dp[j - 1][k - 1][s - xj]
#               : xj <= sのとき、j-1枚目まででsを作る方法と、j-1枚目まででs-xjをつくり、j枚目を選んでk枚にする
#               j > 0, k > 0, s >= xjのとき
#         (4) dp上記以外は無理なので0

    dp[0][0][0] = 1

    for j in range(n + 1):
        for k in range(n + 1):
            for s in range((n + 1) * max(xlist)):
                if j > 0 and xlist[j - 1] > s:
                    dp[j][k][s] = dp[j - 1][k][s]
                elif j > 0 and k > 0 and xlist[j - 1] <= s:
                    dp[j][k][s] = dp[j - 1][k][s] + dp[j - 1][k - 1][s - xlist[j - 1]]

    methods = 0
    for i in range(1, n + 1):
        methods += dp[n][i][i * a]

    print(int(methods))


if __name__ == '__main__':
    submit()
