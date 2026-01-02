#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(c: "List[List[int]]"):
    print(YES if all(
        c[i][j] == c[0][j] + c[i][0] - c[0][0]
        for i in range(1, 3)
        for j in range(1, 3)
    ) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    c = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    solve(c)


if __name__ == '__main__':
    main()
