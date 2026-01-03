#!/usr/bin/env python3
import sys


def solve(N: int, A: int, B: int):
    if A > B:
        print(0)
        return
    
    if N == 1:
        if A==B:
            print(1)
        else:
            print(0)
        return
    
    min_sum = A*(N-1)+B
    max_sum = A+B*(N-1)
    print(max_sum-min_sum+1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)

if __name__ == '__main__':
    main()
