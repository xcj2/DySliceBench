#!/usr/bin/env python3

import sys

def solve(xs):
    xs.sort()
    ans = float('inf')
    for p in range(xs[0], xs[-1] + 1):
        distance = 0
        for x in xs:
            distance += (p - x)**2
        if distance < ans:
            ans = distance
    return ans


def read_int_list():
    return [int(s) for s in sys.stdin.readline().rstrip().split(" ")]


def dprint(*args, **kwargs):
    return
    print(*args, **kwargs)


def main():
    n = int(sys.stdin.readline().rstrip())
    print(solve(read_int_list()))


if __name__ == "__main__":
    main()