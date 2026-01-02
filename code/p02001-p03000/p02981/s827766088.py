#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int):
    train = N * A
    taxi = B

    if train < taxi:
        print(train)
    elif train == taxi:
        print(train)
    else:
        print(taxi)

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
    solve(N, A, B)


if __name__ == '__main__':
    main()
