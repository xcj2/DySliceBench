#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    n = len(str(N))
    dp = [[[0]*2 for _ in range(5)] for _ in range(n+1)]
    # dp[i][j][k] = 上からi桁みたときに0以外がjこあり確定フラグ(0が未確定)がkをみたす数字の数
    number = str(N)
    dp[0][0][0] = 1

    for i in range(n):
        for j in range(4):
            if number[i] == "0":
                #　未確定から未確定
                dp[i+1][j][0] += dp[i][j][0]

                # 確定から確定
                dp[i+1][j+1][1] += dp[i][j][1]*9
                dp[i+1][j][1] += dp[i][j][1]        

                # 未確定から確定(なし)
            else:
                # 未確定から未確定
                dp[i+1][j+1][0] += dp[i][j][0]

                # 確定から確定
                dp[i+1][j+1][1] += dp[i][j][1]*9
                dp[i+1][j][1] += dp[i][j][1]

                # 未確定から確定
                dp[i+1][j+1][1] += dp[i][j][0]*(int(number[i])-1)
                dp[i+1][j][1] += dp[i][j][0]

    print(sum(dp[n][K]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
