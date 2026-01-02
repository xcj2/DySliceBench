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


def bs(a, v):
    ok = len(a)
    ng = -1
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if a[mid] > v:
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N = readi()
    A = sorted(readi(N))
    B = sorted(readi(N))
    C = sorted(readi(N))
    ab = [bs(B, a) for a in A]
    bc = [bs(C, b) for b in B]
    bcount = [N - bc[i] for i in range(N)]
    bcum = arr(N + 1)
    for i in range(N - 1, -1, -1):
        bcum[i] = bcum[i + 1] + bcount[i]
    ans = 0
    for i in range(N):
        ans += bcum[ab[i]]
    print(ans)


if __name__ == "__main__":
    main()
