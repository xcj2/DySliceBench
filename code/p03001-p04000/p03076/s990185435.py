#!/usr/bin/env python3


def key(n):
    m = n % 10
    if m == 0:
        return 10
    else:
        return m


def kiriage(n):
    m = n % 10
    if m == 0:
        return n
    else:
        return n + 10 - m


def solv(a, b, c, d, e):
    times = sorted([a, b, c, d, e], key=key)
    ans = times[0]
    for t in times[1:]:
        ans += kiriage(t)
    return ans


if __name__ == '__main__':

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    ans = solv(a, b, c, d, e)

    print(ans)
