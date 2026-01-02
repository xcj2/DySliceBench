#!/usr/bin/env python
import string
import sys
from collections import Counter
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
    n = readi()
    v = readi(n)
    l1 = v[::2]
    l2 = v[1::2]

    mc1 = Counter(l1).most_common()
    mc2 = Counter(l2).most_common()
    if mc1[0][0] != mc2[0][0]:
        print((n // 2 - mc1[0][1]) + (n // 2 - mc2[0][1]))
    else:
        if len(mc1) > 1 and len(mc2) == 1:
            print((n // 2 - mc1[1][1]) + (n // 2 - mc2[0][1]))
        elif len(mc1) == 1 and len(mc2) > 1:
            print((n // 2 - mc1[0][1]) + (n // 2 - mc2[1][1]))
        elif len(mc1) > 1 and len(mc2) > 1:
            print(
                min(
                    (n // 2 - mc1[1][1]) + (n // 2 - mc2[0][1]),
                    (n // 2 - mc1[0][1]) + (n // 2 - mc2[1][1]),
                )
            )
        else:
            print(n // 2)


if __name__ == "__main__":
    main()
