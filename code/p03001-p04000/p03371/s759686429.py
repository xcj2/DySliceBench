#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int, Y: int):
    ret = 0
    if C * 2 <= A + B:
        ret += min(X, Y) * 2 * C
        if X > Y:
            if C * 2 <= A:
                ret += C * 2 * (X - Y)
            else:
                ret += A * (X - Y)
        else:
            if C * 2 <= B:
                ret += C * 2 * (Y - X)
            else:
                ret += B * (Y - X)

    else:
        ret += A * X + B * Y
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    solve(A, B, C, X, Y)

if __name__ == '__main__':
    main()
