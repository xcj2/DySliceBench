#!/usr/bin/env python3
import sys

def solve(N: int, Z: int, W: int, a: "List[int]"):
    print(max(abs(a[N-1]-a[N-2]),abs(a[N-1]-W)))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, Z, W, a)

if __name__ == '__main__':
    main()
