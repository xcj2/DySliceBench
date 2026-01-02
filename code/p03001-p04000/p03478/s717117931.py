#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: int, B: int):
    tot = 0
    for i in range(N+1):
        s = sum([int(c) for c in str(i)])
        if A <= s <= B:
            tot += i
    print(tot)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)


if __name__ == '__main__':
    main()
