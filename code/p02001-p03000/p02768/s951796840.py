import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    def modcomb(n, c, mod=10 ** 9 + 7):
        if c > n - c:
            c = n - c
        u, d = 1, 1
        for i in range(c):
            u = u * (n - i) % mod
            d = d * (i + 1) % mod
        return u * pow(d, mod - 2,mod)

    mod = 10 ** 9 + 7
    n, a, b = map(int, input().split())
    ans = (pow(2, n) - 1) % mod
    ans = (ans - modcomb(n, a)) % mod
    ans = (ans - modcomb(n, b)) % mod
    print(ans)


resolve()