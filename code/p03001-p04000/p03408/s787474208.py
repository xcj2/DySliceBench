#!/usr/bin/env python3
from collections import Counter
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, s: "List[str]", M: int, t: "List[str]"):
    ctr = Counter(s)
    ctr.subtract(t)
    ((_key, cnt),) = ctr.most_common(1)
    print(max(0, cnt))


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
