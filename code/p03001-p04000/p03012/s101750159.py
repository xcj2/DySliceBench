#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, W: "List[int]"):

    ans = INF
    for i in range(0, N-1):
        ans = min(ans, abs(sum(W[:i+1])-sum(W[i+1:])))

    print(ans)

    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, W)

if __name__ == '__main__':
    main()
