import sys

# お約束
INF = float("inf")
MOD = int(1e9 + 7)
def int1(n):
    return int(n) - 1
def parse(args, *params):
    return tuple(p(v) for p, v in zip(params, next(args).split()))
def debug(*v):
    if __debug__:
        print(*v, file=sys.stderr)

# エントリーポイント
def main(args):
    N, M = parse(args, int, int)
    X = tuple(map(int, next(args).split()))

    x = sorted(X)
    offset_x = [x[n] - x[n - 1] for n in range(1, M)]
    offset_x.sort(reverse=True)

    debug(offset_x)
    print(sum(offset_x[N - 1:]))

if __name__ == '__main__':
    main(iter(sys.stdin.read().split("\n")))
