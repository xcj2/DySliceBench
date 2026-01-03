#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, T: int, t: "List[int]"):

    tot = 0
    for i in range(N-1):
        if t[i+1]-t[i] >= T:
            tot += T
        else:
            tot += t[i+1]-t[i]
    print(tot+T)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    t = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, t)


if __name__ == '__main__':
    main()
