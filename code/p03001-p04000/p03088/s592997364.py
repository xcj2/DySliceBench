#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int):
    mod = 10**9 + 7
    # NG = {AGC,GAC,ACG,ATGC,AGGC,AGTC}
    # (A,C,G,T) = (0,1,2,3)
    # dp[i][j]: 長さiの条件を満たす文字列のうち、末尾がjとなるものの場合の数
    # 初期条件:dp[1] = [1,1,1,1]
    # 答え: dp[N][0] + dp[N][1] + dp[N][2] + dp[N][3]

    dp = [[0]*4 for _ in range(N+1)]
    dp[1] = [1]*4

    for i in range(2,N+1):
        for j in range(4):
            dp[i][j] += sum(dp[i-1]) ##dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
            dp[i][j] %= mod

        # ダメなパターンを引いて補正する
        # 後ろ二文字が"AG","GA"の場合はCを付け足せない
        dp[i][1] -= dp[i-2][0]*1 + dp[i-2][2]*1

        # 後ろ二文字が"AC"の場合はGを付け足せない
        # ~AC となる場合の数は dp[i-2][0] (- dp[i-3][2])
        dp[i][2] -= dp[i-2][0]

        if i >= 3:
            # 後ろ三文字が"ATG","AGG","AGT"となる場合はCを付け足せない
            dp[i][1] -= dp[i-3][0]*3
            dp[i][2] += dp[i-3][2]

    ans = sum(dp[N]) % mod
    print(ans)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
