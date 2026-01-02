#!/usr/bin/env python3


def put(a, k, v):
    if k in a:
        if a[k] != v:
            return False
    else:
        a[k] = v
    return True


def check(n, t, i):
    a = {}
    m = 0
    for j in range(n):
        honest = i >> j & 1
        m += honest
        if not put(a, j+1, honest):
            return 0
        if honest:
            for (k, h) in t[j+1].items():
                if not put(a, k, h if honest else 1 - h):
                    return 0
    return m


def solve(n, t):
    print(max([check(n, t, i) for i in range(1 << n)]))


def main():
    t = {}
    n = int(input())
    for i in range(n):
        a = int(input())
        t[i+1] = {}
        for j in (range(a)):
            x, y = map(int, input().split())
            t[i+1][x] = y
    solve(n, t)


if __name__ == '__main__':
    main()
