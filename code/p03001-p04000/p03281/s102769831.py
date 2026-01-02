#!/usr/bin/env python3
import sys

def count_f(n):
    ret = 0
    for i in range(1, n + 1):
        if n % i == 0:
            ret += 1
    return ret

def solve(N: int):
    ret = 0
    for i in range(1, N + 1):
        if i % 2 == 1 and count_f(i) == 8:
            ret += 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
