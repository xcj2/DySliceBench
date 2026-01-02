#!/usr/bin/env python3
import sys
import bisect
import itertools


def solve(N: int, L: "List[int]"):
    L.sort()
    L = tuple(L)
    ans = 0
    ans = sum([bisect.bisect_left(L, a+L[j]) - j - 1
               for i, a in enumerate(L[:-1], 1) for j in range(i, N)])
    print(ans)
    return


def main():
    def iterate_tokens():
        for sent in sys.stdin:
            for token in sent.split():
                yield token
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L)


if __name__ == '__main__':
    main()
