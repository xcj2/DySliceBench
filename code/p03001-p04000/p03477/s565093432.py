#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, D: int):
    left = A + B
    right = C + D

    if left > right:
        print('Left')
    elif left == right:
        print('Balanced')
    elif left < right:
        print('Right')

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
