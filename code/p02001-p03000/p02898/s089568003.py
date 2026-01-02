#!/usr/bin/env python3
import sys


def solve(N: int, K: int, h: "List[int]"):
    persons = 0

    for _h in h:
        if _h >= K:
            persons += 1

    print(persons)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)


if __name__ == '__main__':
    main()
