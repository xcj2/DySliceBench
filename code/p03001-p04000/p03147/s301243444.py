import sys

# お約束
args = None
INF = float("inf")
MOD = int(1e9 + 7)
def int1(n):
    return int(n) - 1
def parse(*params):
    if len(params) == 1:
        return params[0](next(args))
    return tuple(p(v) for p, v in zip(params, next(args).split()))
def debug(*v):
    if __debug__:
        print(*v, file=sys.stderr)

# エントリーポイント
def main():
    N = parse(int)
    H = [0] + list(map(int, next(args).split()))

    c = 0
    debug(H)
    for h in range(100):
        for n in range(1, N + 1):
            if H[n - 1] - h <= 0 and 0 < H[n] - h:
                c += 1
    print(c)

if __name__ == '__main__':
    args = iter(sys.stdin.read().split("\n"))
    main()
