M = 10 ** 9 + 7

def main():
    n, m = [int(s) for s in input().split()]

    print(solve(m, n, 10 ** 9 + 7))

def solve(m, n, mod):
    r = 1

    for _, c in get_prime_factors(m):
        r = r * mod_comb(c + n - 1, c, mod) % mod
    return r

def mod_comb(n, k, m):
    r = 1
    for i in range(1, k + 1):
        r = r * (n - k + i) * mod_inv(i, m) % m
    return r

def mod_inv(n, m):
    r0, r1 = n, m
    x, y, u, v = 1, 0, 0, 1

    while r1:
        k, r0, r1 = r0 // r1, r1, r0 % r1
        x, y, u, v = u, v, x - k * u, y - k * v

    if r0 != 1:
        raise ValueError

    return x

def get_prime_factors(n):
    from itertools import count, takewhile
    r = n

    for i in takewhile(lambda x: x * x <= r, count(2)):
        c = 0
        while r % i == 0:
            c += 1
            r //= i
        yield i, c

    if r != 1:
        yield r, 1

main()
