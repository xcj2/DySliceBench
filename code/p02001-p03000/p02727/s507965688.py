#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(X: int, Y: int, A: int, B: int, C: int, p: "List[int]", q: "List[int]", r: "List[int]"):
    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)
    xy = sorted(p[:X] + q[:Y])
    ans = sum(p[:X]) + sum(q[:Y])
    z = 0
    while z < X + Y and z < C and xy[z] < r[z]:
        ans += r[z] - xy[z]
        z += 1
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    q = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    r = [int(next(tokens)) for _ in range(C)]  # type: "List[int]"
    solve(X, Y, A, B, C, p, q, r)


if __name__ == '__main__':
    main()
