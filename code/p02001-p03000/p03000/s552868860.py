#!/usr/bin/env python3
import sys
from itertools import accumulate
INF = float("inf")


def solve(N: int, X: int, L: "List[int]"):
    D = [0]+list(accumulate(L))
    count = 0
    for d in D:
        if d <= X:
            count += 1
    print(count)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, L)


if __name__ == '__main__':
    main()
