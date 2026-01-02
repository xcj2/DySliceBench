#!/usr/bin/env python3
from collections import defaultdict
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, P: "List[int]", Y: "List[int]"):
    cities = sorted(
        (Yi, Pi, i)
        for i, (Pi, Yi) in enumerate(zip(P, Y))
    )
    ans = [""] * M
    cnt = defaultdict(int)
    for Yi, Pi, i in cities:
        cnt[Pi] += 1
        ans[i] = "%06d%06d" % (Pi, cnt[Pi])

    for ansi in ans:
        print(ansi)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        P[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, P, Y)


if __name__ == '__main__':
    main()
