#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def sqrt(n: int):
    lb = 0
    rb = n + 1
    while lb + 1 < rb:
        m = (lb + rb) // 2
        if m * m > n:
            rb = m
        else:
            lb = m
    return lb


def solve(Q: int, A: "List[int]", B: "List[int]"):
    for Ai, Bi in zip(A, B):
        a = sqrt(Ai * Bi)
        b = a + 1 if a * (a + 1) <= Ai * Bi else a

        def f(a: int, b: int):
            m = a + b - 2
            if a * b == Ai * Bi:
                m -= b - a + 1
                if {a, b} == {Ai, Bi}:
                    m += 1
            return m

        print(max(f(a, b), f(a, b - 1)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    A = [int()] * (Q)  # type: "List[int]"
    B = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(Q, A, B)


if __name__ == '__main__':
    main()
