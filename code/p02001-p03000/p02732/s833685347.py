#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, A: "List[int]"):
    counts = {}
    for v in A:
        if not v in counts:
            counts[v] = 0
        counts[v] += 1
    cnts = list(counts.values())
    s = 0
    for c in cnts:
        s += (c * (c - 1)) // 2
    for v in A:
        ret = s
        if counts[v] > 1:
            ret -= counts[v] - 1
        print(ret)
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
