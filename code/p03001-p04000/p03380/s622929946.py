#!/usr/bin/env python3
import sys


def solve(n: int, a: "List[int]"):
    mx = max(a)
    a.sort()
    l = -1
    r = n
    while r - l > 1:
        m = (r + l) // 2
        if a[m] > (mx + 1) // 2:
            r = m
        else:
            l = m
    target = (mx + 1) // 2
    if r == n - 1 or abs(target - a[l]) < abs(target - a[r]):
        print(mx, a[l])
    else:
        print(mx, a[r])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = [ int(next(tokens)) for _ in range(n) ]  # type: "List[int]"
    solve(n, a)

if __name__ == '__main__':
    main()
