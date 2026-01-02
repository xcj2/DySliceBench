# お約束
INF = float("inf")
MOD = int(1e9 + 7)
def int1(n):
    return int(n) - 1
def parse(args, *params):
    return tuple(p(v) for p, v in zip(params, next(args).split()))

# エントリーポイント
def main(args):
    N, A, B, C = parse(args, int, int, int, int)
    L = tuple(int(next(args)) for _ in range(N))

    def solve(n, l, a, b, c, cost):
        if n == 0:
            if not all((a, b, c)): return INF
            return abs(A - a) + abs(B - b) + abs(C - c) + cost - 30
        r = []
        r += [solve(n - 1, l, a, b, c, cost)]
        r += [solve(n - 1, l, a + l[n - 1], b, c, cost + 10)]
        r += [solve(n - 1, l, a, b + l[n - 1], c, cost + 10)]
        r += [solve(n - 1, l, a, b, c + l[n - 1], cost + 10)]
        return min(r)

    print(solve(N, L, 0, 0, 0, 0))

import sys
if __name__ == '__main__':
    main(iter(sys.stdin.read().split("\n")))
