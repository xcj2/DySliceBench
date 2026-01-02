#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(a: int, b: int, c: int, d: int):
    if abs(a-c) <= d:
        print("Yes")
    elif abs(a-b) <= d and abs(b-c) <= d:
        print("Yes")
    else:
        print("No")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    solve(a, b, c, d)


if __name__ == '__main__':
    main()
