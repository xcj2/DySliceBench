#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, W: int, s: "List[str]"):
    print(YES if all(
        any(
            s[y + dy][x + dx] == "#"
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if 0 <= x + dx < W and 0 <= y + dy < H
        )
        for y in range(H)
        for x in range(W)
        if s[y][x] == "#"
    ) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(H)]  # type: "List[str]"
    solve(H, W, s)


if __name__ == '__main__':
    main()
