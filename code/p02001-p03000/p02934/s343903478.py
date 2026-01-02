#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    result = 0
    for i in range(N):
        result += 1 / A[i]

    if N == 1:
        print(A[0])
    else:
        print(float(1 / result))

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == "__main__":
    main()
