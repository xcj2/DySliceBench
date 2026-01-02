#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, p: "List[float]"):
    # prob[i][j]はi枚まで投げてj枚表になる確率
    prob = [[0]*(N+1) for _ in range(N+1)]
    prob[0][0] = 1
    for i in range(N):
        for j in range(N+1):
            prob[i+1][j] = prob[i][j]*(1-p[i])
            if j-1 >= 0:
                prob[i+1][j] += prob[i][j-1]*p[i]
    print(sum(prob[N][N//2+1:]))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [float(next(tokens)) for _ in range(N)]  # type: "List[float]"
    solve(N, p)


if __name__ == '__main__':
    main()
