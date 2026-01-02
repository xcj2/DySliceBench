#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, p: "List[int]"):
    ans = 0
    s = 0
    for i, pi in enumerate(p):
        if i + 1 == pi:
            s = 1 - s
            ans += s
        else:
            s = 0
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, p)


if __name__ == '__main__':
    main()
