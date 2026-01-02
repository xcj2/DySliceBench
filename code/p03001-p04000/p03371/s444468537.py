#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int, Y: int):
    if A+B < 2*C:
        print(X*A+Y*B)
    else:
        if X >= Y:
            print(min(Y*(2*C) + A*(X-Y),X*2*C))
        else:
            print(min(X*(2*C)+B*(Y-X), Y*2*C))

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
