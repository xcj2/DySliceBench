#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: int, B: int, X: "List[int]"):
    tot = 0
    for i in range(N-1):
        sub = X[i+1]-X[i]
        if sub*A < B:
            tot += sub*A
        else:
            tot += B
    print(tot)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, X)


if __name__ == '__main__':
    main()
