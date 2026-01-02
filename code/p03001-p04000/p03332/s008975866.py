def prepare(n, MOD):
    f = 1
    for m in range(1, n + 1):
        f *= m
        f %= MOD

    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv

    return f, invs


def ex_euclid(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1

    while c1 != 0:
        m = c0 % c1
        q = c0 // c1

        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)

    return c0, a0, b0


def solve(n, a, b, k):
    MOD = 998244353
    fn, invs = prepare(n, MOD)

    if a < b:
        a, b = b, a
    c, x, y = ex_euclid(a, b)
    d, m = divmod(k, c)
    if m != 0:
        return 0
    ac, bc = a // c, b // c
    x, y = x * d, y * d
    if x < 0:
        f = ((x % bc) - x) // bc
        x += bc * f
        y -= ac * f
    else:
        f, x = divmod(x, bc)
        y += ac * f
    if y > n:
        f = (y - n - 1) // ac + 1
        x += bc * f
        y -= ac * f
    # print(x, y, a * x + b * y)

    ans = 0
    base = fn * fn % MOD
    while x <= n and y >= 0:
        tmp = base * invs[x]
        tmp %= MOD
        tmp *= invs[n - x]
        tmp %= MOD
        tmp *= invs[y]
        tmp %= MOD
        tmp *= invs[n - y]
        ans += tmp
        ans %= MOD
        x += bc
        y -= ac

    return ans


n, a, b, k = map(int, input().split())

print(solve(n, a, b, k))
