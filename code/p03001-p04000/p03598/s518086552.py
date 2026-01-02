#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, K: int, x: "List[int]"):
    ans = 0
    for i in range(N):
        ans += min(x[i], K-x[i])
    print(ans*2)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, x)


if __name__ == '__main__':
    main()
