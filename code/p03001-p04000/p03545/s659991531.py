#!/usr/bin/env python3
from itertools import product
import sys


def solve(ABCD: str):
    A, B, C, D = ABCD
    for ops in product(["+", "-"], repeat=3):
        expr = "{1}{0[0]}{2}{0[1]}{3}{0[2]}{4}".format(ops, A, B, C, D)
        if eval(expr) == 7:
            print(expr + "=7")
            return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    ABCD = next(tokens)  # type: str
    solve(ABCD)


if __name__ == '__main__':
    main()
