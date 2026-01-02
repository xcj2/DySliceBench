#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(H: int, W: int, S: "List[str]"):
    d = [[0] * W for _ in range(H)]
    for y in range(H):
        x = 0
        while x < W:
            while x < W and S[y][x] == "#":
                x += 1
            xstt = x
            while x < W and S[y][x] == ".":
                x += 1
            xend = x
            for x2 in range(xstt, xend):
                d[y][x2] += xend - xstt
    for x in range(W):
        y = 0
        while y < H:
            while y < H and S[y][x] == "#":
                y += 1
            ystt = y
            while y < H and S[y][x] == ".":
                y += 1
            yend = y
            for y2 in range(ystt, yend):
                d[y2][x] += yend - ystt

    print(max(max(r) for r in d) - 1)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, S)


if __name__ == '__main__':
    main()
