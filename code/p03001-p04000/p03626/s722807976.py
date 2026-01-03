#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


MOD = 1000000007  # type: int


def solve(N: int, S: "List[str]"):
    ans = 1
    pdtype = 0
    i = 0
    while i < N:
        dtype = 2 if S[0][i] != S[1][i] else 1
        ans = {
            (0, 1): lambda: 3,
            (0, 2): lambda: 6,
            (1, 1): lambda: ans * 2,
            (1, 2): lambda: ans * 2,
            (2, 1): lambda: ans,
            (2, 2): lambda: ans * 3,
        }[pdtype, dtype]() % MOD
        i += dtype
        pdtype = dtype
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(2)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
