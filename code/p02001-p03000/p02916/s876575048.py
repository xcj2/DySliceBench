#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    last = -999
    satis = 0
    for now in A:
        if now-1 == last:
            satis += C[last-1]
        satis += B[now-1]
        last = now
    print(satis)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N - 1)]  # type: "List[int]"
    solve(N, A, B, C)


if __name__ == '__main__':
    main()
