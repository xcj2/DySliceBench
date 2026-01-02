#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


def solve(N: int, S: "List[str]"):
    c = Counter()
    for s in S:
        c[s] += 1

    m = -1
    for key in c:
        if c[key] > m:
            m = c[key]
    ans = []
    for key in c:
        if c[key] == m:
            ans.append(key)
    ans.sort()
    for line in ans:
        print(line)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)


if __name__ == '__main__':
    main()
