# -*- coding: utf-8 -*-
"""



"""
import sys


from collections import deque
from functools import lru_cache

@lru_cache(maxsize=None)
def dig_left(n, q):
    res = [0]
    for di in range(1, min(n, len(q))+1):
        bu = n - di
        dig = list(q[:di])
        dig.sort()
        while bu and dig and dig[0] < 0:
            dig.pop(0)
            bu -= 1
        res.append(sum(dig))
    return max(res)


@lru_cache(maxsize=None)
def dig_right(n, q):
    res = [0]
    for di in range(1, min(n, len(q))+1):
        bu = n - di
        dig = list(q[-di:])
        dig.sort()
        while bu and dig and dig[0] < 0:
            dig.pop(0)
            bu -= 1
        res.append(sum(dig))
    return max(res)


def solve(N, K, V):
    ans = [0]
    limit = sum([v for v in V if v > 0])
    for left in range(K+1):
        q = deque(V)
        right = K - left
        l_dig = dig_left(left, tuple(V))
        r_dig = dig_right(right, tuple(V))
        ans.append(min(limit, l_dig+r_dig))
    return max(ans)


def main(args):
    N, K = map(int, input().split())
    V = [int(v) for v in input().split()]
    ans = solve(N, K, V)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
