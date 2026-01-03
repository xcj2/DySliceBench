#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(N: int, A: "List[int]"):
    c = Counter(A)
    daburi = 0
    for k in c:
        if c[k] % 2 == 1:
            c[k] = 1
        elif c[k] % 2 == 0:
            c[k] = 2
            daburi += 1
    if daburi % 2 == 1:
        print(len(c)-1)
    else:
        print(len(c))

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
