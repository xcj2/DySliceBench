#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, H: int, a: "List[int]", b: "List[int]"):
    ma = max(a)
    b.sort(reverse=True)
    i = 0
    for i in range(N):
        if b[i] <= ma:
            i -= 1
            break
        H -= b[i]
        if H <= 0:
            print(i + 1)
            return
    print(i + 1 + -(-H // ma))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, H, a, b)


if __name__ == '__main__':
    main()
