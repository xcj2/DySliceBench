#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(A: int, B: int):
    from math import ceil
    print(ceil((B-A)/(A-1))+1)
    # n = A
    # i = 1
    # while n < B:
    #     n += (A-1)
    #     i += 1

    # print(i)

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
