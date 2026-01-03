#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, s: "List[int]"):
    tot = sum(s)
    if tot % 10 != 0:
        print(tot)
        return
    m = INF
    for x in s:
        if x % 10 == 0:
            continue
        if x < m:
            m = x
    if m != INF:
        print(tot-m)
    else:
        print(0)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, s)


if __name__ == '__main__':
    main()
