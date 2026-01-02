#!/usr/bin/env python3
import sys


def solve(N: int, P: int):
    if N == 1:
        print(P)
        return
    ret = 1
    i = 2
    while i * i <= P:
        count = 0
        while P % i == 0:
            P //= i
            count += 1
        if count > 0:
            #print(i, count)
            for _ in range(count // N):
                ret *= i
        i += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    solve(N, P)

if __name__ == '__main__':
    main()
