#!/usr/bin/env python3
import sys


def solve(M: int, D: int):
    count = 0
    for m in range(1, M+1):
        for d in range(1, D+1):
            d_1 = d % 10
            d_10 = d // 10
            if d_1 >= 2 and d_10 >= 2 and d_1*d_10 == m:
                count += 1
    print(count)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(M, D)

if __name__ == '__main__':
    main()