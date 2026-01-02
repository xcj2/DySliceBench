import functools
import itertools

import os
import sys

sys.setrecursionlimit(10000)
INF = float('inf')


def debug(fn):
    if not os.getenv('LOCAL'):
        return fn

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        print('DEBUG: {}({}) -> '.format(
            fn.__name__,
            ', '.join(
                list(map(str, args)) +
                ['{}={}'.format(k, str(v)) for k, v in kwargs.items()]
            )
        ), end='')
        print(ret)
        return ret

    return wrapper


def count_mp(target, sizes):
    return (len(sizes) - 1) * 10 + abs(target - sum(sizes))


N, A, B, C = map(int, input().split())
sizes = []
for _ in range(N):
    sizes.append(int(input()))

ans = INF
for allocs in itertools.product('abc_', repeat=N):
    a = []
    b = []
    c = []
    mp = 0
    for i, al in enumerate(allocs):
        if al == 'a':
            a.append(sizes[i])
        if al == 'b':
            b.append(sizes[i])
        if al == 'c':
            c.append(sizes[i])
    if not a or not b or not c:
        continue
    ans = min(ans, count_mp(A, a) + count_mp(B, b) + count_mp(C, c))
    if ans == 0:
        break
print(ans)
