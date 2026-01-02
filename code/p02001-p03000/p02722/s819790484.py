#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int):
    if N < 5:
        print(N - 1)
        return
    i = 2
    ret = 2
    while i * i <= N:
        tmp = N
        while tmp % i == 0:
            tmp //= i
        tmp %= i
        if tmp == 1:
            ret += 1

        if N % i == 1 and i * i + 1 != N:
            ret += 1
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
    solve(N)

if __name__ == '__main__':
    main()
