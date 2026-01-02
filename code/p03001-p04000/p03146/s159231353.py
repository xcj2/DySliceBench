#!/usr/bin/env python3
import sys


def solve(s: int):
    memo = [-1] * 1000001
    for i in range(1000001):
        if memo[s] >= 0:
            ret = i + 1
            break
        memo[s] = i
        if s % 2 == 0:
            s //= 2
        else:
            s = 3 * s + 1
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = int(next(tokens))  # type: int
    solve(s)

if __name__ == '__main__':
    main()
