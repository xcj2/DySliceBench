#!/usr/bin/env python
import string
import sys
from itertools import chain, dropwhile, takewhile

INF = float("inf")


def read(
    *shape, f=int, it=chain.from_iterable(sys.stdin), whitespaces=set(string.whitespace)
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


def readi(*shape):
    return read(*shape)


def readi1(*shape):
    return [i - 1 for i in readi(*shape)]


def readf(*shape):
    return read(*shape, f=float)


def reads(*shape):
    return read(*shape, f=str)


def arr(*shape, fill_value=0):
    if len(shape) == 1:
        return [fill_value] * shape[0]
    elif len(shape) == 2:
        return [[fill_value] * shape[1] for _ in range(shape[0])]


def dbg(**kwargs):
    print(
        ", ".join("{} = {}".format(k, repr(v)) for k, v in kwargs.items()),
        file=sys.stderr,
    )


def main():
    N, K = readi(2)
    h = readi(N)
    h.extend([0] * K)
    dp = arr(N + K, fill_value=INF)
    dp[0] = 0
    for i in range(N):
        for j in range(K):
            dp[i + j + 1] = min(dp[i + j + 1], dp[i] + abs(h[i + j + 1] - h[i]))
    print(dp[N - 1])


if __name__ == "__main__":
    main()
