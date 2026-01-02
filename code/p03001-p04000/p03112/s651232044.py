# お約束
INF = float("inf")
MOD = int(1e9 + 7)
def int1(n):
    return int(n) - 1
def parse(args, *params):
    return tuple(p(v) for p, v in zip(params, next(args).split()))

from bisect import bisect_right as bsr

# エントリーポイント
def main(args):
    A, B, Q = parse(args, int, int, int)
    S = list(int(next(args)) for _ in range(A))
    T = list(int(next(args)) for _ in range(B))
    X = tuple(int(next(args)) for _ in range(Q))

    s = [-INF] + S + [INF]
    t = [-INF] + T + [INF]
    for x in X:
        sr = bsr(s, x)
        sl = sr - 1
        tr = bsr(t, x)
        tl = tr - 1
        min_cost = INF
        for st in [s[sl], s[sr]]:
            for tt in [t[tl], t[tr]]:
                min_cost = min(min_cost, abs(st - x) + abs(tt - st))
                min_cost = min(min_cost, abs(tt - x) + abs(tt - st))
        print(min_cost)

import sys
if __name__ == '__main__':
    main(iter(sys.stdin.read().split("\n")))
