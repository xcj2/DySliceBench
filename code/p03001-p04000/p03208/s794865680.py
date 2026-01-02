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

    diff_h = tuple(h[l + K - 1] - h[l] for l in range(N - K + 1))

    print(min(diff_h))

if __name__ == '__main__':
    args = iter(sys.stdin.read().split("\n"))
    main()
