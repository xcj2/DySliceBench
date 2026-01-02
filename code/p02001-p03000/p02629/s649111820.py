#!/usr/bin/env python3
import bisect
import collections
import sys

sys.setrecursionlimit(1000000)
ACMOD = 1000000007
INF = 1 << 62


def solve(N: int):
    base = 26
    # z 26
    # aa 27
    # ab 28
    if N == 1:
        print("a")
        return
    rans = []
    for i in range(100000):
        if N == 0:
            break
        N -= 1
        if i == 0:
            rans.append(chr(N % base + ord('a')))
            N = N // base
        else:
            rans.append(chr((N) % base + ord('a')))
            N = N // base
    print("".join(reversed(rans)))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)


if __name__ == '__main__':
    main()
