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


from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


from collections import defaultdict


def main():
    n = readi()
    shougen = defaultdict(list)
    for i in range(n):
        a = readi()
        for _ in range(a):
            x, y = readi(2)
            x -= 1
            shougen[i].append((x, y))

    ans = 0
    for ps in powerset(range(n)):
        valid = True
        for p in ps:
            for x, y in shougen[p]:
                if y == 1 and x not in ps:
                    valid = False
                if y == 0 and x in ps:
                    valid = False
        if valid:
            ans = max(ans, len(ps))
    print(ans)


if __name__ == "__main__":
    main()
