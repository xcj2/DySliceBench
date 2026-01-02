import sys
from string import ascii_lowercase

lim = 10**5 + 100
mod = 10**9 + 7


def main():
    n, m = map(int, input().split())

    f = [1]*(lim + 1)
    for i in range(2, lim + 1):
        f[i] = (i * f[i-1]) % mod
    rf = [1]*(lim + 1)
    rf[lim] = pow(f[lim], mod - 2, mod)
    for i in range(lim - 1, 1, -1):
        rf[i] = ((i+1) * rf[i+1]) % mod

    def comb(n, k):
        return f[n] * rf[k] * rf[n-k] % mod

    divs = factorize(m)

    ans = 1

    for p, c in divs:
        ans *= comb(n - 1 + c, n - 1)
        ans %= mod

    print(ans)


def factorize(n):
    res = []
    for i in range(2, n + 1):
        if i*i > n:
            break
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        res.append((i, cnt))

    if n > 1:
        res.append((n, 1))

    return res


if __name__ == '__main__':
    main()
