#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    ans = [0]*N
    for aa, bb in zip(a, b):
        ans[aa-1] += 1
        ans[bb-1] += 1
    print(*ans, sep="\n")

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == '__main__':
    main()
