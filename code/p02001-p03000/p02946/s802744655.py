#!/usr/bin/env python3
import sys
import numpy as np


def solve(K: int, X: int):
    start = X - K + 1
    end = X + K - 1
    for i in range(start, end + 1):
        if i == end:
            print(i)
        else:
            print(i, end=" ")

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(K, X)


if __name__ == "__main__":
    main()
