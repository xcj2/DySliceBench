#!/usr/bin/env python
import string
import sys
from itertools import chain, dropwhile, takewhile


def read(
    f, *shape, it=chain.from_iterable(sys.stdin), whitespaces=set(string.whitespace)
):
    def read_word():
        w = lambda c: c in whitespaces
        nw = lambda c: c not in whitespaces
        return f("".join(takewhile(nw, dropwhile(w, it))))

    if not shape:
        return read_word()
    elif len(shape) == 1:
        return [read_word() for _ in range(shape[0])]
    elif len(shape) == 2:
        return [[read_word() for _ in range(shape[1])] for _ in range(shape[0])]


def arr(*shape, fill_value=0):
    if len(shape) == 1:
        return [fill_value] * shape[fill_value]
    elif len(shape) == 2:
        return [[fill_value] * shape[1] for _ in range(shape[0])]


def dbg(**kwargs):
    print(
        ", ".join("{} = {}".format(k, repr(v)) for k, v in kwargs.items()),
        file=sys.stderr,
    )


def main():
    dp = arr(31)
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, 31):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    while True:
        n = read(int)
        if n == 0:
            break
        print(dp[n] // 10 // 365 + 1)


if __name__ == "__main__":
    main()

