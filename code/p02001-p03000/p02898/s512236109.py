#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, h: "List[int]"):
    counter = 0
    for hh in h:
        if hh >= K:
            counter += 1
    print(counter)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)


if __name__ == '__main__':
    main()
