#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, H: "List[int]"):

    ans = 0
    minh = -INF
    for h in H:
        if h >= minh:
            ans += 1
            minh = h
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, H)


if __name__ == '__main__':
    main()
