#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, D: int, E: int):
    m = [A, B, C, D, E]
    print(sum(-(-mi // 10) * 10 for mi in m) - max(-mi % 10 for mi in m))


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
