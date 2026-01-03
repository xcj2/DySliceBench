#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(x: int, y: int):
    table = [0]*13
    table[2] = 2
    table[4] = 1
    table[6] = 1
    table[9] = 1
    table[11] = 1
    if table[x] == table[y]:
        yes()
    else:
        no()
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(x, y)


if __name__ == '__main__':
    main()
