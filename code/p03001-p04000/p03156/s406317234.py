#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)
INF = 1<<32


def solve(N: int, A: int, B: int, P: "List[int]"):
    P.sort()
    from bisect import bisect_left, bisect_right
    x = bisect_right(P, A)
    y = bisect_right(P, B)

    print(min(x, y-x, N-y))

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
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, P)

if __name__ == '__main__':
    main()
