import bisect
import collections
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 32


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


H, W = lmi()
S = [input().strip() for _ in range(W)]

import functools


@functools.lru_cache(maxsize=None)
def solve(h, w, last_b=False):
    if h < 0 or w < 0:
        return INF
    if h == 0 and w == 0:
        return int(S[0][0] == '#') and (not last_b)
    b = bool(S[h][w] == '#')
    if b:
        return min(solve(h - 1, w, last_b=True) + (not last_b),
                   solve(h, w - 1, last_b=True) + (not last_b),
                   )
    return min(
        solve(h - 1, w, last_b=False),
        solve(h, w - 1, last_b=False),
        solve(h - 1, w, last_b=True) + 1,
        solve(h, w - 1, last_b=True) + 1,
        # solve(h - 1, w, last_b=False) + b,
        # solve(h, w - 1, last_b=False) + b,
    )


print(solve(H - 1, W - 1))
