#!/usr/bin/env python3
import sys


def solve(N: int, W: "List[int]"):
    wsum = sum(W)
    S1 = 0
    S2 = wsum
    diff = sys.maxsize
    for i in range(N - 1):
      S1 += W[i]
      S2 -= W[i]
      diff = min(diff, abs(S1-S2))
    print(diff)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, W)

if __name__ == '__main__':
    main()
