#!/usr/bin/env python3


def count1(n):
    return bin(n).count("1")


def tobin(ns):
    rv = 0
    for n in ns:
        rv += 1 << (n-1)
    return rv


def solv(n, m, ss, z1s):
    ss = list(map(tobin, ss))
    ans = 0
    for on in range(2**n):
        # print('on=', on)
        ok = 1
        for i in range(m):
            # print('ss[i], on, z1s', ss[i], on, z1s[i])
            if count1(ss[i] & on) % 2 != z1s[i]:
                ok = 0
                break
        ans += ok
    return ans


if __name__ == '__main__':

    n, m = map(int, input().split())

    ss = []
    for _ in range(m):
        s = list(map(int, input().split()))
        s = s[1:]
        ss.append(s)

    z1s = list(map(int, input().split()))

    ans = solv(n, m, ss, z1s)
    print(ans)
