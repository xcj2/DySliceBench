#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, K: int, h: "List[int]"):
    print(len(
        [i for i in h if i >= K]
    ))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)

if __name__ == '__main__':
    main()
