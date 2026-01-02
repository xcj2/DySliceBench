#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    x, y, a, b, c = MI()
    p = LI()
    q = LI()
    r = LI()

    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)

    p_selected = p[:x]
    q_selected = q[:y]

    ans = [*p_selected, *q_selected]

    ans.sort()
    i = 0

    while i < x + y and i < c and ans[i] < r[i]:
        ans[i] = r[i]
        i += 1

    print(sum(ans))


main()
