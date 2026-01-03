#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    inf = float("inf")
    sc = [-inf] * N
    sc[0] = 0
    ans = 0
    for i in range(2 * N):
        for ai, bi, ci in zip(a, b, c):
            ai -= 1
            bi -= 1
            sc[bi] = max(sc[bi], sc[ai] + ci)
        if i == N - 1:
            ans = sc[N - 1]
    if ans < sc[N - 1]:
        print("inf")
        return
    print(sc[N - 1])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, M, a, b, c)


if __name__ == '__main__':
    main()
