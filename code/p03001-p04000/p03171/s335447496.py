#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, a: "List[int]"):

    dp = [[0]*N for _ in range(N)]
    for sub in range(N):
        turn = sub % 2
        for i in range(N-sub):
            j = i+sub
            # i ~ jの数列に対して操作
            if i == j:
                if (N-sub+1) % 2 == 0:
                    dp[i][i] = a[i]
                else:
                    dp[i][i] = -a[i]
                continue

            if (N-sub+1) % 2 == 0:    # 先手番
                dp[i][j] = max(a[i] + dp[i+1][j], a[j]+dp[i][j-1])
            else:               # 後手番
                dp[i][j] = min(-a[i] + dp[i+1][j], -a[j]+dp[i][j-1])
    print(dp[0][N-1])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
