#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, X: "List[int]"):

    m = INF
    for i in range(1, 101):
        tot = 0
        for j in range(N):
            tot += (X[j]-i)**2
        m = min(tot, m)
    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X)


if __name__ == '__main__':
    main()
