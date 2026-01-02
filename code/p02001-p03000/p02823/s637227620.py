#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, A: int, B: int):
    if (B-A) % 2 == 0:
        print(min((B-A)//2, min(max(A, B)-1, N-min(A, B))))
    else:
        # 偶奇をすらすパターン
        m = A + (B-A-1)//2
        m = min(m, N-B+1+(B-A-1)//2)
        print(m)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)


if __name__ == '__main__':
    main()
