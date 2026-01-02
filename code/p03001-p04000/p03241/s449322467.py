#!/usr/bin/env python3

import bisect


def divisors(n):
    ds = []
    for i in range(1, int(n ** 0.5) + 1):
        d, m = divmod(n, i)
        if m == 0:
            ds.append(i)
            ds.append(d)
    ds.sort()
    return ds


def find_ge(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError


def solve(n, m):
    ds = divisors(m)
    t = find_ge(ds, n)
    return m // t


def main():
    n, m = (int(z) for z in input().split())
    res = solve(n, m)
    print(res)


if __name__ == '__main__':
    main()