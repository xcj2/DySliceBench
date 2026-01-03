#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, T: int, A: "List[int]"):

    amin, amin_i = (INF, -1)
    gmax = 0
    cand = []

    for i, a in enumerate(A):
        if a < amin:
            amin = a
            amin_i = i
        else:
            if a-amin > gmax:
                gmax = a-amin
                cand = [(gmax, amin_i, i)]
            elif a-amin == gmax:
                cand.append((gmax, amin_i, i))
    print(len(cand))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, A)


if __name__ == '__main__':
    main()
