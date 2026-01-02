import sys
from operator import itemgetter as ig
from collections import defaultdict as dd

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
    N, K = parse(int, int)
    H = [parse(int) for _ in range(N)]

    h = sorted(H)
    l, r = 0, K

    sum_h = [0]
    for n in range(1, N):
        sum_h += [sum_h[-1] + (h[n] - h[n - 1])]
    debug(sum_h)

    diff_h = tuple(sum_h[l + K - 1] - sum_h[l] for l in range(N - K + 1))
    debug(diff_h)
    print(min(diff_h))

if __name__ == '__main__':
    args = iter(sys.stdin.read().split("\n"))
    main()
