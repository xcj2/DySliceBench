#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def main():
    num_psgr, bus_cap, max_itvl = read_h()
    arv_tms = sorted(read_v(num_psgr))

    num_bus = 1
    cur_bus_cap = bus_cap - 1
    deadline = arv_tms[0] + max_itvl
    for t in arv_tms[1:]:
        if t <= deadline and cur_bus_cap >= 1:
            cur_bus_cap -= 1
        else:
            num_bus += 1
            cur_bus_cap = bus_cap - 1
            deadline = t + max_itvl

    print(num_bus)


if __name__ == '__main__':
    main()
