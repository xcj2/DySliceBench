#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(A: int, B: int):

    ans = 0
    if A > B:
        ans += A
        A -= 1
    else:
        ans += B
        B -= 1

    if A > B:
        ans += A
        A -= 1
    else:
        ans += B
        B -= 1

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
    solve(A, B)


if __name__ == '__main__':
    main()
