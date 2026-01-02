#!/usr/bin/env python3
import sys
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(s: str, t: str):
    s = "".join(sorted(list(s)))
    t = "".join(sorted(list(t), reverse=True))
    if s < t:
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
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)


if __name__ == '__main__':
    main()
