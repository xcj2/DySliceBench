#!/usr/bin/env python3
import sys


def solve(K: int, A: int, B: int):
    if B - A <= 2 or K <= A:
        print(K + 1)
        return
    K -= A - 1
    ret = A + (K // 2) * (B - A) + K % 2
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(K, A, B)

if __name__ == '__main__':
    main()
