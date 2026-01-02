#!/usr/bin/env python3
import sys
INF = float("inf")


def argmax(a):
    m, n = -(1 << 31), -1
    for i, v in enumerate(a):
        if m < v:
            m, n = v, i
    return m, n


def solve(N: int, A: "List[int]"):
    m, mi = argmax(A)
    m2, mi2 = argmax(A[:mi]+A[mi+1:])
    for i in range(N):
        if i == mi:
            print(m2)
        else:
            print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)


if __name__ == '__main__':
    main()
