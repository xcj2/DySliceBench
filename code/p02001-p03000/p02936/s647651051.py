import sys
from math import factorial, ceil, floor
from bisect import bisect_right as bsr
from operator import itemgetter as ig
from collections import defaultdict as dd
from collections import deque

# お約束
args = None
INF = float("inf")
MOD = int(1e9 + 7)
def int1(n):
    return int(n) - 1
def input():
    return next(args)
def parse(*params):
    if len(params) == 1:
        return params[0](next(args))
    return tuple(p(v) for p, v in zip(params, next(args).split()))
def debug(*v):
    if __debug__:
        print(*v, file=sys.stderr)

# エントリーポイント
def main():
    N, Q = parse(int, int)
    edges = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = parse(int, int)
        edges[a] += [b]
        edges[b] += [a]
    vals = [0] * (N + 1)
    for _ in range(Q):
        p, x = parse(int, int)
        vals[p] += x

    counter = [0] * (N + 1)
    que = deque()
    que.append((1, 0))
    alr = [False] * (N + 1)
    while que:
        v, x = que.pop()
        alr[v] = True
        counter[v] += x + vals[v]
        for n in edges[v]:
            if not alr[n]:
                que.append((n, counter[v]))

    print(*counter[1:])

if __name__ == '__main__':
    args = iter(sys.stdin.read().split("\n"))
    main()
