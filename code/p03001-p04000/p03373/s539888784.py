#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int, X: int, Y: int):
    ans = 1e20
    for i in range(max(X, Y) + 1):
        a = max(X-i, 0)
        b = max(Y-i, 0)
        c = 2*i
        ans = min(ans, A*a + B*b + C*c)
    return ans

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    print(solve(A, B, C, X, Y))

if __name__ == '__main__':
    main()
