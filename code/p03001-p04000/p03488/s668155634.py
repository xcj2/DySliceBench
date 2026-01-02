#!/usr/bin/env python3
import sys
INF = float("inf")
from collections import defaultdict


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(s: str, x: int, y: int):
    N = len(s)
    s = [len(FF) for FF in s.split("T")]
    sX = s[0::2]                # 空となるケースに注意
    sY = s[1::2]                # 空となるケースに注意
    # print(sX, sY)

    # sXを足すか引くかして、xにたどり着くことができるか
    DPx = defaultdict(bool)
    DPx[sX[0]] = True
    for c in sX[1:]:
        DPnext = defaultdict(bool)
        for key in DPx:
            DPnext[key-c] = True
            DPnext[key+c] = True
        DPx = DPnext

    DPy = defaultdict(bool)
    DPy[0] = True
    for c in sY:
        DPnext = defaultdict(bool)
        for key in DPy:
            DPnext[key-c] = True
            DPnext[key+c] = True
        DPy = DPnext

    if DPx[x] and DPy[y]:
        yes()
    else:
        no()
    return


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
