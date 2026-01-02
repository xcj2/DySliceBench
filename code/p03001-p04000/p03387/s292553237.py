#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    mx = max(A, B, C)
    tmp = 0
    tmp += mx - A
    tmp += mx - B
    tmp += mx - C
    if tmp % 2 == 0:
        ret = tmp // 2
    else:
        ret = (tmp + 3) // 2
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
    solve(A, B, C)

if __name__ == '__main__':
    main()
