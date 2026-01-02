# AC: msec(Python3)
from math import factorial
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

MOD = 10**9+7

def cmb(n, r):
    if n < 0 or r < 0:
        return 0
    if r > n:
        return 0

    r = min(n-r, r)
    res = 1
    for i in range(r):
        res *= n - i

    return res // factorial(r)


def prime_factorization(n):
    d = []
    i, e = 2, 0  # factor, exponent
    while i * i <= n:
        while n % i == 0:
            n //= i
            e += 1
        if e > 0:
            d.append((i, e))
        i += 1
        e = 0
    if n > 1:
        d.append((n, 1))
    return d


def main():
    N,M = map(int, readline().split())

    d = prime_factorization(M)

    ans = 1
    for i, e in d:
        ans *= cmb(N-1+e, e)
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
