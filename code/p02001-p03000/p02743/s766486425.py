#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(a: int, b: int, c: int):
    if c-a-b > 0 and (4*a*b < (c-a-b)**2):
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
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    solve(a, b, c)


if __name__ == '__main__':
    main()
