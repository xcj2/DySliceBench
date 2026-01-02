#!/usr/bin/env python3
from itertools import product
import sys
try:
    from typing import List
except ImportError:
    pass


def bsearch1(i: int, a: "List[int]"):
    lb = 0
    rb = len(a) + 1
    while lb + 1 < rb:
        m = (lb + rb) // 2
        if a[m] > i:
            rb = m
        else:
            lb = m
    return lb


def bsearch2(i: int, a: "List[int]"):
    lb = 0
    rb = len(a) + 1
    while lb + 1 < rb:
        m = (lb + rb) // 2
        if a[m] > i:
            lb = m
        else:
            rb = m
    return lb


def solve(N: int, A: "List[int]"):
    cumleft = [0] * (N + 1)
    for i in range(N):
        cumleft[i + 1] = cumleft[i] + A[i]

    cumright = [0] * (N + 1)
    for i in reversed(range(N)):
        cumright[i] = cumright[i + 1] + A[i]

    mleft = [bsearch1(cumi // 2, cumleft) for cumi in cumleft]
    mright = [bsearch2(cumi // 2, cumright) for cumi in cumright]
    ans = cumright[0]
    for i in range(2, N + 1 - 2):
        j1s = {mleft[i] - 1, mleft[i], mleft[i] + 1} - {0, i}
        j2s = {mright[i] - 1, mright[i], mright[i] + 1} - {i, N}
        for j1, j2 in product(j1s, j2s):
            p = cumleft[j1]
            q = cumleft[i] - cumleft[j1]
            r = cumleft[j2] - cumleft[i]
            s = cumright[j2]
            ans = min(ans, max(p, q, r, s) - min(p, q, r, s))
    print(ans)


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
