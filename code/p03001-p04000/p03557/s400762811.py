#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def f(b: "List[int]", l1: "List[int]", l2: "List[int]"):
    result = [0] * len(l2)
    i = 0
    t = 0
    for j, l2j in enumerate(l2):
        while i < len(l1) and l1[i] < l2j:
            t += b[i]
            i += 1
        result[j] = t
    return result


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    A.sort()
    B.sort()
    C.sort()
    ba = [1] * N
    bb = f(ba, A, B)
    bc = f(bb, B, C)
    print(sum(bc))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C)


if __name__ == '__main__':
    main()
