#!/usr/bin/env python3
import sys
INF = float("inf")


def GCD(a, b):
    if a == 0:
        return b
    else:
        return GCD(b % a, a)


def LCM(a, b):
    return a*b//GCD(a, b)


def solve(N: int, T: "List[int]"):
    ans = 1
    for i in range(N):
        ans = LCM(ans, T[i])

    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T)


if __name__ == '__main__':
    main()
