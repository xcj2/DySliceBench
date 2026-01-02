#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, D: int, E: int):
    R = [A, B, C, D, E]
    mn = 10
    ret = 0
    count = 0
    for r in R:
        if r % 10 > 0 and r % 10 < mn:
            mn = r % 10
        if r % 10 == 0:
            count += 1
        ret += (r // 10) * 10
    ret += (5 - count) * 10
    ret -= 10 - mn
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
    E = int(next(tokens))  # type: int
    solve(A, B, C, D, E)

if __name__ == '__main__':
    main()
