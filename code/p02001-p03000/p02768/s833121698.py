import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    # https://atcoder.jp/contests/abc156/submissions/11621672
    def modpow(a, b, mod=10 ** 9 + 7):
        ret = 1
        while b > 0:
            if b % 2 == 1:
                ret = ret * a % mod
            a = a * a % mod
            b //= 2
        return ret

    def modcomb(n, c, mod=10 ** 9 + 7):
        if c > n - c:
            c = n - c
        u, d = 1, 1
        for i in range(c):
            u = u * (n - i) % mod
            d = d * (i + 1) % mod
        return u * modpow(d, mod - 2) % mod

    mod = 10 ** 9 + 7
    n, a, b = map(int, input().split())
    ans = (modpow(2, n) - 1) % mod
    ans = (ans - modcomb(n, a)) % mod
    ans = (ans - modcomb(n, b)) % mod
    print(ans)


resolve()