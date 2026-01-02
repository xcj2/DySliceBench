#!/usr/bin/env python
import string
import sys
from itertools import chain, dropwhile, takewhile


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
    return [i - 1 for i in read(*shape)]


def readf(*shape):
    return read(*shape, f=float)


def reads(*shape):
    return read(*shape, f=str)


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
    sys.setrecursionlimit(100000)
    n, q = readi(2)
    par = arr(n + 1)
    for i in range(len(par)):
        par[i] = i

    def find(x):
        if x == par[x]:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y

    def same(x, y):
        return find(x) == find(y)

    for _ in range(q):
        com, x, y = readi(3)
        if com == 0:
            unite(x, y)
        else:
            print(1 if same(x, y) else 0)


if __name__ == "__main__":
    main()

