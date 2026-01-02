#!/usr/bin/env python3
from collections import Counter
from itertools import chain
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, a: "List[int]"):
    ctr = Counter(chain.from_iterable(
        (ai - 1, ai, ai + 1)
        for ai in a
    ))
    print(ctr.most_common(1)[0][1])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
