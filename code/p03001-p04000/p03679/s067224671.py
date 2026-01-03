#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(X: int, A: int, B: int):
    if B-A <= 0:
        print("delicious")
    elif B-A <= X:
        print("safe")
    else:
        print("dangerous")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(X, A, B)


if __name__ == '__main__':
    main()
