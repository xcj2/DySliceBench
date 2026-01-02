#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, m = MI()
    connected = []
    for i in range(m):
        row = LI()
        swithes = row[1:]
        connected.append(swithes)
    p = LI()
    ans = 0
    for i in range(2 ** n):
        i_str = format(i, f"0{n}b")
        is_ok = True
        for m_idx in range(m):
            sum_1 = 0
            for swith in connected[m_idx]:
                if i_str[swith - 1] == "1":
                    sum_1 += 1

            if sum_1 % 2 != p[m_idx]:
                is_ok = False
                break

        if is_ok:
            ans += 1

    print(ans)


main()
