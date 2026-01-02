#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, W: "List[str]"):
    print(YES if len(set(W)) == N and all(
        W[i][-1] == W[i + 1][0]
        for i in range(N - 1)
    ) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, W)


if __name__ == '__main__':
    main()
