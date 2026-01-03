#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 5  # type: int


def yes():
    print("YES")  # type: str


def no():
    print("NO")  # type: str


def solve(A: int, B: int, C: int):
    tot = 0
    for _ in range(100):
        tot += A
        if tot % B == C:
            yes()
            return
    no()
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
    solve(A, B, C)


if __name__ == '__main__':
    main()
