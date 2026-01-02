#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


def solve(N: int, a: "List[int]"):
    total_xor = 0
    for v in a:
        total_xor = total_xor ^ v

    # for v in a:
    #     print(total_xor ^ v)
    print(" ".join((str(total_xor^v) for v in a)))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
