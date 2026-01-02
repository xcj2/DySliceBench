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
    V, E = readi(2)
    G = arr(V, V, fill_value=INF)
    for i in range(V):
        G[i][i] = 0
    for _ in range(E):
        s, t, d = readi(3)
        G[s][t] = d

    for k in range(V):
        for i in range(V):
            for j in range(V):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if G[i][j] > G[i][k] + G[k][j]:
                    print("NEGATIVE CYCLE")
                    return

    for i in range(V):
        print(" ".join(map(lambda n: "INF" if n == INF else str(n), G[i])))


if __name__ == "__main__":
    main()

