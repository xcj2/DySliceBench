#!/usr/bin/env python3
from itertools import permutations
import sys


def solve(A: int, B: int, C: int):
    m = 0
    for n1, n2, n3 in permutations([A, B, C]):
        exp1 = "%d+%d%d" % (n1, n2, n3)
        exp2 = "%d%d+%d" % (n1, n2, n3)
        m = max(m, eval(exp1), eval(exp2))
    print(m)


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
