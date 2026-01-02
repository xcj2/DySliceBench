#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(H: int, W: int, S: "List[str]"):

    def isbomb(i: int, j: int):
        return 0 <= i < H and 0 <= j < W and S[i][j] == "#"

    ds = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

    for i, Si in enumerate(S):
        print("".join(
            c if c == "#" else
            str(sum(
                isbomb(i + di, j + dj)
                for di, dj in ds
            ))
            for j, c in enumerate(Si)
        ))


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
