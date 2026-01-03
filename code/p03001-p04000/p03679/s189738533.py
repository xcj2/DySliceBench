#!/usr/bin/env python3
import sys


def solve(X: int, A: int, B: int):
    expire = B - A

    if expire <= 0:
        print('delicious')
        return
    elif X - expire >= 0:
        print('safe')
        return
    else:
        print('dangerous')
        return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(X, A, B)


if __name__ == '__main__':
    main()
