#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def bisect(a: "List[int]", x: int):
    lb = 0
    rb = len(a) + 1
    while lb + 1 < rb:
        m = (lb + rb) // 2
        if a[m - 1] >= x:
            rb = m
        else:
            lb = m
    return lb


def solve(A: int, B: int, Q: int, s: "List[int]", t: "List[int]", x: "List[int]"):
    for xk in x:
        i = bisect(s, xk)
        j = bisect(t, xk)
        m = float("inf")
        if i > 0 and j > 0:
            m2 = max(xk - s[i - 1], xk - t[j - 1])
            m = min(m, m2)
        if i > 0 and j < B:
            ld = xk - s[i - 1]
            rd = t[j] - xk
            m2 = min(ld + ld + rd, ld + rd + rd)
            m = min(m, m2)
        if i < A and j > 0:
            rd = s[i] - xk
            ld = xk - t[j - 1]
            m2 = min(ld + ld + rd, ld + rd + rd)
            m = min(m, m2)
        if i < A and j < B:
            m2 = max(s[i] - xk, t[j] - xk)
            m = min(m, m2)
        print(m)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    t = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(A, B, Q, s, t, x)


if __name__ == '__main__':
    main()
