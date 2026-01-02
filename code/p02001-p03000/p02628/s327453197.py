#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


def solve(N: int, K: int, p: "List[int]"):
    p.sort()
    print(sum(p[:K]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, p)


if __name__ == '__main__':
    main()
