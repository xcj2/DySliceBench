# https://atcoder.jp/contests/abc154/tasks/abc154_e


def digit(N, M):
    """
    :param N: 0 <= n <= N の整数 (※ 下限が 1 の場合は返り値を -= 1 等する)
    :param M: 状態数（例: 0<= (0の個数) <= M）

    dp[0][i][*]: 上からi桁目までが N と一致
    dp[1][i][*]: 上からi桁目までで N である事が確定
    dp[*][*][j]: 状態 j の個数（今回は j = (0 の個数) ）
    """
    def f(j,k):
        """状態 j からの繊維。 i+1 桁目の数( = j)に依存"""
        return min2(j + (k != 0), M - 1)

    L = len(N)
    dp = [[[0] * M for i in range(L + 1)] for j in range(2)]

    dp[0][0][0] = 1
    for i in range(L):
        for j in range(M):
            for k in range(10):
                if k < N[i]:
                    dp[1][i+1][f(j, k)] += dp[0][i][j] + dp[1][i][j]
                elif k == N[i]:
                    dp[0][i+1][f(j, k)] += dp[0][i][j]
                    dp[1][i+1][f(j, k)] += dp[1][i][j]
                else:
                    dp[1][i+1][f(j, k)] += dp[1][i][j]

    return dp[0][L][K] + dp[1][L][K]

##########################################################################################

N = list(map(int, input().strip()))     # 整数を桁毎のリストとして読み込む
K = int(input())
M = K + 2                               # 状態数

def min2(x,y):
    return x if x < y else y

print(digit(N, M))