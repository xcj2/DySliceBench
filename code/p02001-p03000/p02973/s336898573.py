#!/usr/bin/env python3
import sys
from collections import deque
from bisect import bisect_left

def solve(N: int, A: "List[int]"):
    b = deque([A[0]])
    for a in A[1:]:
        if a <= b[0]:
            b.appendleft(a)
        else:
            idx = bisect_left(b, a)
            b[idx-1] = a
    print(len(b))
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
