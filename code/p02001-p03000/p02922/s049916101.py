#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(A: int, B: int):
    ret = 0
    if B == 1:
        ret = 0
    else:
        for i in range(100):
            if A + (A - 1) * i >= B:
                ret = i + 1
                break
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
