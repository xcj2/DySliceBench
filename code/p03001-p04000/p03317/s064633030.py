#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, A: "List[int]"):
    m = min(A)
    m1 = A.index(m)
    ans = -(-m1 // (K - 1))
    c = ans * (K - 1) + 1
    while c < N:
        while A[c] == m:
            c += 1
        c += K - 1
        ans += 1
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)


if __name__ == '__main__':
    main()
