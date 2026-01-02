import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def input():
    return sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    A = list(map(int, input().split()))

    S = [0]
    for a in A:
        S.append(S[-1] + a)

    cnt = {}
    for s in S:
        if s not in cnt:
            cnt[s] = 1
        else:
            cnt[s] += 1

    ans = 0
    for v in cnt.values():
        if v >= 2:
            ans += cmb(v, 2)

    print(ans)


if __name__ == '__main__':
    main()
