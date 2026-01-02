#!/usr/bin/env python3
import sys


def solve(A: int, B: int):

    plug_num = 1
    plugable_num = A

    while plugable_num < B:
        plugable_num += A - 1
        plug_num += 1

    if B == 1:
        print(0)
    else:
        print(plug_num)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)


if __name__ == "__main__":
    main()
