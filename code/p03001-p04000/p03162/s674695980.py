#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    DP = [[0]*(N+1) for _ in range(3)]
    for i in range(N):
        # 行動a[i]を選ぶ場合
        DP[0][i+1] = max(DP[1][i], DP[2][i])+a[i]
        # 行動b[i]を選ぶ場合
        DP[1][i+1] = max(DP[2][i], DP[0][i])+b[i]
        # 行動c[i]を選ぶ場合
        DP[2][i+1] = max(DP[0][i], DP[1][i])+c[i]
    print(max(DP[0][N], DP[1][N], DP[2][N]))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    c = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, a, b, c)


if __name__ == '__main__':
    main()
