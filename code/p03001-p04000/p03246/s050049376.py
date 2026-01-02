#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(n: int, v: "List[int]"):
    c0 = Counter(v[0::2])
    c1 = Counter(v[1::2])

    # print(c0)
    # print(c1)
    c0[0] = 0
    c1[0] = 0

    mc0 = c0.most_common(2)
    mc1 = c1.most_common(2)

    v0, v1 = -INF, -INF

    if mc0[0][0] == mc1[0][0]:
        if mc0[0][1] + mc1[1][1] < mc0[1][1] + mc1[0][1]:
            v0 = mc0[1][1]
            v1 = mc1[0][1]
        else:
            v0 = mc0[0][1]
            v1 = mc1[1][1]
    else:
        v0 = mc0[0][1]
        v1 = mc1[0][1]

    print(n - v0-v1)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    v = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, v)


if __name__ == '__main__':
    main()
