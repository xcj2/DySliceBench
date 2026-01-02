#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def solve(H: int, W: int):
    if H == 1 or W == 1:
        print(1)
        return
    elif H % 2 == 1 and W % 2 == 1:
        print(H*W//2+1)
    else:
        print(H*W//2)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    solve(H, W)


if __name__ == '__main__':
    main()
