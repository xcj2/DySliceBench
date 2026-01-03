#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, A: "List[str]", B: "List[str]"):
    print(YES if any(all(
        A[y + dy][x + dx] == B[dy][dx]
        for dx in range(M) for dy in range(M)
    ) for x in range(N - M + 1) for y in range(N - M + 1)) else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(N)]  # type: "List[str]"
    B = [next(tokens) for _ in range(M)]  # type: "List[str]"
    solve(N, M, A, B)


if __name__ == '__main__':
    main()
