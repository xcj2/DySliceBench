#!/usr/bin/env python
# coding: utf-8

from collections import Counter

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n = ri()
    la = rli()
    da = Counter()
    for a in la:
        da[a] += 1

    # 全て0
    if 0 in da and da[0] == n:
        print("Yes")
        return
    # それ以外は、個数が3の倍数でないとダメ
    if n % 3 != 0:
        print("No")
        return

    # 0: n/3個、x: 2*n/3個
    if len(da) == 2:
        if 0 in da and da[0] == n / 3:
            print("Yes")
            return

    # x, y, z: n/3個
    if len(da) == 3:
        x, y, z = da.keys()
        if (x ^ y == z) and da[x] == n/3 and da[y] == n/3:
            print("Yes")
            return

    # それ以外
    print("No")


if __name__ == '__main__':
    main()
