#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, h: "List[int]"):
    DP = [0]*N
    DP[1] = abs(h[1]-h[0])
    for i in range(2, N):
        DP[i] = min(DP[i-1]+abs(h[i]-h[i-1]),
                    DP[i-2]+abs(h[i]-h[i-2]))
    print(DP[N-1])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, h)


if __name__ == '__main__':
    main()
