#!/usr/bin/env python3
import sys


def solve(Q: int, H: int, S: int, D: int, N: int):
    x = min(4*Q,2*H,S)
    y = D

    if x<=y/2:
        print(N*x)
    else:
        if N&1:
            print(N//2*y+x)
        else:
            print(N//2*y)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(Q, H, S, D, N)

if __name__ == '__main__':
    main()
