#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from collections import defaultdict
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(w: str):
    d = defaultdict(int)
    for c in w:
        d[c] += 1
    flag = True
    for k, v in d.items():
        if v % 2 == 1:
            flag = False
            break
    if flag:
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
    w = next(tokens)  # type: str
    solve(w)


if __name__ == '__main__':
    main()
