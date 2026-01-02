#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(s: str, x: int, y: int):
    try:
        k = s.index("T")
    except ValueError:
        k = len(s)
    x -= k
    s = s[k:]
    xs = []
    ys = []
    d = 0
    v = 0
    for c in s:
        if c == "T":
            if v != 0:
                if d == 0:
                    xs.append(v)
                else:
                    ys.append(v)
            d = 1 - d
            v = 0
        else:
            v += 1
    if v != 0:
        if d == 0:
            xs.append(v)
        else:
            ys.append(v)
    mx = sum(xs)
    dpx = [0] * (mx + 1)
    dpx[0] = 1
    for xi in xs:
        for j in reversed(range(xi, len(dpx))):
            dpx[j] |= dpx[j - xi]
    my = sum(ys)
    dpy = [0] * (my + 1)
    dpy[0] = 1
    for yi in ys:
        for j in reversed(range(yi, len(dpy))):
            dpy[j] |= dpy[j - yi]
    if (
        -mx <= x <= mx and (mx - x) % 2 == 0 and dpx[(mx - x) // 2] and
        -my <= y <= my and (my - y) % 2 == 0 and dpy[(my - y) // 2]
    ):
        print(YES)
    else:
        print(NO)



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(s, x, y)


if __name__ == '__main__':
    main()
