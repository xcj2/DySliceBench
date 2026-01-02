#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]", d: "List[int]"):
    rs = sorted(zip(a, b))
    bs = sorted(zip(c, d))
    for bx, by in bs:
        mi = -1
        my = -1
        for i, (rx, ry) in enumerate(rs):
            if not (rx < bx and ry < by):
                continue
            if my < ry:
                mi = i
                my = ry
        if mi != -1:
            del rs[mi]
    print(N - len(rs))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    c = [int()] * (N)  # type: "List[int]"
    d = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, a, b, c, d)


if __name__ == '__main__':
    main()
