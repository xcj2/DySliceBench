#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, V: "List[int]", C: "List[int]"):
    ans = 0
    for v, c in zip(V, C):
        if v-c > 0:
            ans += v-c
    print(ans)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    V = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, V, C)


if __name__ == '__main__':
    main()
