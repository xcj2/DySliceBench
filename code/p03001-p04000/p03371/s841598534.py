#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(A: int, B: int, C: int, X: int, Y: int):
    ans = 0
    if 2*C < A+B:     # C買うフェイズ
        ge = min(X, Y)
        ans += C*2*ge
        X -= ge
        Y -= ge

    if X > 0:                   # コスパよくAを集める
        if 2*C < A:
            ans += C*2*X
        else:
            ans += A*X
    if Y > 0:
        if 2*C < B:
            ans += C*2*Y
        else:
            ans += B*Y
    print(ans)

    return


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
    solve(A, B, C, X, Y)


if __name__ == '__main__':
    main()
