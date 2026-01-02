#!/usr/bin/env python3
import sys


def solve(K: int, X: int):
    res = [X]

    # right
    for i in range(X + 1, X + K):
        res.append(i)

    # left
    for i in range(X - 1, X - K, -1):
        res.append(i)

    for i, x in enumerate(sorted(res)):
        print(x, end='')
        if not res.__len__() == i + 1:
            print(end=' ')

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    solve(K, X)


if __name__ == '__main__':
    main()

