#!/usr/bin/env python3
import sys


def solve(N: int, K: int, A: "List[int]"):
    for i in range(1, N + 1):
        if K * i - (i - 1) >= N:
            ret = i
            break
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
