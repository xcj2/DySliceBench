#!/usr/bin/env python
import string
import sys
from itertools import chain, dropwhile, takewhile, permutations


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
        return [fill_value] * shape[fill_value]
    elif len(shape) == 2:
        return [[fill_value] * shape[1] for _ in range(shape[0])]


def dbg(**kwargs):
    print(
        ", ".join("{} = {}".format(k, repr(v)) for k, v in kwargs.items()),
        file=sys.stderr,
    )


def main():
    N, M, R = readi(3)
    rs = readi1(R)

    G = arr(N, N, fill_value=10 ** 10)
    for i in range(N):
        G[i][i] = 0

    for _ in range(M):
        a, b, c = readi(3)
        G[a - 1][b - 1] = c
        G[b - 1][a - 1] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    ans = 10 ** 10
    for perm in permutations(rs):
        tmp = 0
        for i in range(len(perm) - 1):
            tmp += G[perm[i]][perm[i + 1]]
        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
