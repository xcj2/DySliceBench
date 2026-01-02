#!/usr/bin/env python3
import sys


def GCD(a, b):
    # a < b
    if a == 0:
        return b
    else:
        return GCD(b % a, a)


def solve(N: int, X: int, x: "List[int]"):
    y = [abs(item-X) for item in x]
    ans = y[0]
    for a in y:
        ans = GCD(a, ans)

    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, x)


if __name__ == '__main__':
    main()
