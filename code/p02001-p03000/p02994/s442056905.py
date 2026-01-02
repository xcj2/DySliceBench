#!/usr/bin/env python3
import sys


def solve(N: int, L: int):
    abs_val = sys.maxsize
    flavor = 0
    for i in range(N):
        a = L + i
        flavor += a
        if abs(a) < abs_val:
            abs_val = abs(a)
            index = i
    print(flavor - (L + index))
    
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, L)

if __name__ == '__main__':
    main()
