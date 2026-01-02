#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(N: int, s: "List[str]", M: int, t: "List[str]"):
    m = 0
    rec = ""
    sc = Counter(s)
    st = Counter(t)
    for c, v in sc.items():
        if m < v - st[c]:
            rec = c
            m = v - st[c]
    print(m)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    M = int(next(tokens))  # type: int
    t = [next(tokens) for _ in range(M)]  # type: "List[str]"
    solve(N, s, M, t)


if __name__ == '__main__':
    main()
