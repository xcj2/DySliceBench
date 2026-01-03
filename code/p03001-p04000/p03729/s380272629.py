#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("YES")  # type: str


def no():
    print("NO")  # type: str


def solve(A: str, B: str, C: str):
    if A[-1] == B[0] and B[-1] == C[0]:
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
    A = next(tokens)  # type: str
    B = next(tokens)  # type: str
    C = next(tokens)  # type: str
    solve(A, B, C)


if __name__ == '__main__':
    main()
