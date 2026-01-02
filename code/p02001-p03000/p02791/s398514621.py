#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, P: "List[int]"):

    count = 0
    m = INF
    for p in P:
        if m > p:
            count += 1
            m = p
    print(count)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P)


if __name__ == '__main__':
    main()
