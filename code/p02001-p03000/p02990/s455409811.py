import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    mod = 10 ** 9 + 7
    N, K = map(int, input().split())


    from operator import mul
    from functools import reduce


    # 未読
    def comb(n, r):
        if n < r:
            return 0
        else:
            r = min(n - r, r)
            if r == 0:
                return 1
            over = reduce(mul, range(n, n - r, -1))
            under = reduce(mul, range(1, r + 1))
            return over // under

    for i in range(1, K + 1):
        print((comb(K - 1, i - 1) * comb(N - K + 1, i)) % mod)


resolve()