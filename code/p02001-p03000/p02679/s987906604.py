import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def egcd(a: int, b: int):
    """
    A solution of ax+by=gcd(a,b). Returns
    (gcd(a,b), (x, y)).
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def modinv(a: int, mod: int = 10**9 + 7):
    """
    Returns a^{-1} modulo m.
    """
    g, x, y = egcd(a, mod)
    if g > 1:
        raise Exception('{}^(-1) mod {} does not exist.'.format(a, mod))
    else:
        return x % mod


def modpow(a: int, n: int, mod: int = 10**9 + 7):
    """
    Returns a^n mod m. (-inf < n < inf)
    """
    if a in [-1, 0, 1]:
        if a == -1:
            return 1 if n & 1 == 0 else mod - 1
        else:
            return a

    x, k = (a % mod, n) if n >= 0 else (modinv(a, mod), -n)

    ret = 1
    while k > 0:
        if k & 1 == 1:
            ret = ret * x % mod
        x = (x**2) % mod
        k = k >> 1

    return ret


def main():
    N = gete(int)

    d = dict()
    z = 0

    for _ in range(N):
        a, b = geta(int)
        if a == b == 0:
            z += 1
            continue

        if a != 0 and b != 0:
            g, _, _ = egcd(a, b)
            ai, bi = a // g, b // g
            c1 = (ai, bi) if ai > 0 else (-ai, -bi)
            c2 = (bi, -ai) if bi > 0 else (-bi, ai)
        elif a == 0:
            c1 = (0, 1)
            c2 = (1, 0)
        elif b == 0:
            c1 = (1, 0)
            c2 = (0, 1)

        if c1 in d:
            d[c1][0] += 1
        elif c2 in d:
            d[c2][1] += 1
        else:
            d[c1] = [1, 0]

    mod = 1000000007
    ans = 1
    for k in d:
        n = modpow(2, d[k][0], mod)
        m = modpow(2, d[k][1], mod)
        ans = ans * (n + m - 1) % mod

    ans = (ans + z - 1) % mod

    print(ans)


if __name__ == "__main__":
    main()