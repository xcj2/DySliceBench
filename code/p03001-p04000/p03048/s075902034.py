#!/usr/bin/env python3
import sys


def solve(R: int, G: int, B: int, N: int):
    ret = 0
    for r in range(N // R + 1):
        rest = N - r * R
        for g in range(rest // G + 1):
            if (rest - g * G) % B == 0:
                ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(R, G, B, N)

if __name__ == '__main__':
    main()
