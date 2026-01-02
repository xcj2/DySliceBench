#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(n: int, a: "List[int]"):
    a.sort(reverse=True)
    r0 = a[0]
    r1 = a[1]
    h = r0 // 2
    for v in a[1:]:
        if abs(v - h) < abs(r1 - h):
            r1 = v
    print(r0, r1)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
