#!/usr/bin/env python3
import sys


def solve(N: int, K: int):
    count = 0

    if K % 2 == 0:
        count += (N//K)**3
        # a,b,c == 0 mod K//2
        count += (N//(K//2) - N//K)**3
    else:
        count += (N//K)**3
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
