#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, x: "List[float]", u: "List[str]"):
    rate = 380000.0
    print(sum(xi * (rate if ui == "BTC" else 1.0) for xi, ui in zip(x, u)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [float()] * (N)  # type: "List[float]"
    u = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        x[i] = float(next(tokens))
        u[i] = next(tokens)
    solve(N, x, u)


if __name__ == '__main__':
    main()
