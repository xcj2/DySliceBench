#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(N: int, a: "List[int]"):
    c = Counter()
    for aa in a:
        c[min(aa//400, 8)] += 1

    tot = 0
    for k in c:
        if k == 8:
            continue
        else:
            tot += 1
    if tot == 0 and c[8] > 0:
        print(1, c[8])
    else:
        print(tot, tot+c[8])

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
