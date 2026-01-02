#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, D: int):
    if A + B > C + D:
        ret = 'Left'
    elif A + B < C + D:
        ret = 'Right'
    else:
        ret = 'Balanced'
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)

if __name__ == '__main__':
    main()
