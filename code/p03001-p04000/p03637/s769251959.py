#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, a: "List[int]"):
    n2 = sum(1 for ai in a if ai % 4 == 0)
    n0 = sum(1 for ai in a if ai % 2 == 1)
    ans = NO
    if n2 + 1 == n0 and n2 + n0 == N:
        ans = YES
    elif n2 >= n0:
        ans = YES
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
