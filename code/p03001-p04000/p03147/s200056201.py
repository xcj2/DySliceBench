#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, h: "List[int]"):
    ans = 0
    for k in range(max(h)):
        r = [i for i in range(N) if h[i] > k]
        a = 0
        j = 0
        while j < len(r):
            a += 1
            while j + 1 < len(r) and r[j + 1] == r[j] + 1:
                j += 1
            j += 1
        ans += a
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, h)


if __name__ == '__main__':
    main()
