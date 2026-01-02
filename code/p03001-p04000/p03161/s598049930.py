#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, h: "List[int]"):
    DP = [INF]*N
    DP[0] = 0
    for i in range(1, N):
        for j in range(1, K+1):
            if i-j >= 0:
                DP[i] = min(DP[i], DP[i-j]+abs(h[i]-h[i-j]))
    print(DP[N-1])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)


if __name__ == '__main__':
    main()
