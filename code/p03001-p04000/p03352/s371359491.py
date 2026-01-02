#!/usr/bin/env python3
import sys


def ilog(b: int, x: int):
    if b == 1:
        return 0
    lb = 0
    rb = x.bit_length()
    while lb + 1 < rb:
        m = (lb + rb) // 2
        if b ** m <= x:
            lb = m
        else:
            rb = m
    return lb


def solve(X: int):
    print(max(
        b ** ilog(b, X)
        for b in range(1, X + 1)
        if b ** 2 <= X
    ))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)


if __name__ == '__main__':
    main()
