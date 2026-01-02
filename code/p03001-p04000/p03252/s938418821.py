#!/usr/bin/env python3
from collections import defaultdict
import sys


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str, T: str):
    d1 = defaultdict(set)
    for i, si in enumerate(S):
        d1[si].add(i)
    d2 = defaultdict(set)
    for i, ti in enumerate(T):
        d2[ti].add(i)
    print(
        YES if
        set(frozenset(s) for s in d1.values()) ==
        set(frozenset(s) for s in d2.values())
        else NO)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(S, T)


if __name__ == '__main__':
    main()
