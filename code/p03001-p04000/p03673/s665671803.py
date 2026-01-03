#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(n: int, a: "List[int]"):
    if n % 2 == 0:
        b = list(reversed(a[::2]))+a[1::2]
    else:
        b = list(reversed(a[1::2]))+a[::2]
    print(*reversed(b), sep=" ")

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, a)


if __name__ == '__main__':
    main()
