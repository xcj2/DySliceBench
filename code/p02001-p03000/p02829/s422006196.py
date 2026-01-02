#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(A: int, B: int):
    ret = 0
    if 1 in [A, B] and 2 in [A, B]:
        ret = 3
    if 1 in [A, B] and 3 in [A, B]:
        ret = 2
    if 2 in [A, B] and 3 in [A, B]:
        ret = 1
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
    solve(A, B)

if __name__ == '__main__':
    main()
