#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    if N > M:
        N, M = M, N
    ret = 0
    if N == 1:
        if M == 1:
            ret = 1
        else:
            ret = M - 2
    else:
        ret = (N - 2) * (M - 2)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
