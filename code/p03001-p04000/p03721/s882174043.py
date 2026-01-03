#!/usr/bin/env python3
from collections import defaultdict
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, K: int, a: "List[int]", b: "List[int]"):
    d = defaultdict(int)
    for ai, bi in zip(a, b):
        d[ai] += bi
    for k, v in sorted(d.items()):
        K -= v
        if K <= 0:
            print(k)
            return
    assert False


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, K, a, b)


if __name__ == '__main__':
    main()
