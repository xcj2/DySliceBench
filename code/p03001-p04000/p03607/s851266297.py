#!/usr/bin/env python3
import sys
from bisect import bisect_left
INF = float("inf")


def solve(N: int, A: "List[int]"):
    X = []
    for a in A:
        i = bisect_left(X, a)
        if i < len(X) and X[i] == a:
            X.pop(i)
        else:
            X.insert(i, a)
    print(len(X))

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


if __name__ == '__main__':
    main()
