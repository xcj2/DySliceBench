#!/usr/bin/env python3
import sys
from functools import reduce
from operator import add
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int):
    if N % reduce(add, [int(c) for c in str(N)]) == 0:
        yes()
    else:
        no()
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
