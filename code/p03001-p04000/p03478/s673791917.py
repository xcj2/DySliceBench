#!/usr/bin/env python3
import sys

def sum_dig(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret

def solve(N: int, A: int, B: int):
    ret = 0
    for i in range(1, N + 1):
        if A <= sum_dig(i) <= B:
            ret += i
    print(ret)
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
