#!/usr/bin/env python3
import sys


def v(a: int, b: int, c: int):
    if a < b:
        a, b = b, a
    if c % a == 0:
        return c
    minr = c
    for va in range(c // a + 1):
        minr = min(minr, (c - va * a) % b)
        if minr == 0:
            break
    return c - minr


def solve(A: int, B: int, C: int, D: int, E: int, F: int):
    ansa = A * 100
    anss = 0
    for w in range(1, F // 100 + 1):
        w2 = v(B, A, w)
        if w != w2:
            continue
        s = min(w2 * E, F - w2 * 100)
        s2 = v(D, C, s)
        a2 = s2 + w2 * 100
        if a2 > F:
            continue
        # anss / ansa < s2 / a2
        if anss * a2 < ansa * s2:
            ansa, anss = a2, s2
    print(ansa, anss)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    solve(A, B, C, D, E, F)


if __name__ == '__main__':
    main()
