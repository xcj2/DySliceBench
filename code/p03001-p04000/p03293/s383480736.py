#!/usr/bin/env python3
import sys
import itertools
import collections
import functools
import math
from queue import Queue
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(S: str, T: str):
    for i in range(len(S)):
        kari = S[i:]+S[:i]
        if kari == T:
            yes()
            return
    no()
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)


if __name__ == '__main__':
    main()
