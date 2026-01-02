#!/usr/bin/env python3
import sys


def solve(N: int, L: int):
    ls = [L + x for x in range(0, N)]

    if L > 0:
        del ls[0]
        print(sum(ls))

        return

    elif ls.__contains__(0):
        print(sum(ls))

        return
    else:
        del ls[-1]
        print(sum(ls))

        return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word

    tokens = iterate_tokens()

    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    solve(N, L)


if __name__ == '__main__':
    main()
