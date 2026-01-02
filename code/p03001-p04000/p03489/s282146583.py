#!/usr/bin/env python3
import sys
import collections


def solve(N: int, a):
    c = collections.Counter(a)
    z = 0
    for k, v in c.items():
        if v - k < 0:
            z += v
        else:
            z += v - k
    print(z)


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
