#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("YES")  # type: str


def no():
    print("NO")  # type: str


def solve(r: int, g: int, b: int):
    if int(str(r)+str(g)+str(b)) % 4 == 0:
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
    r = int(next(tokens))  # type: int
    g = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(r, g, b)


if __name__ == '__main__':
    main()
