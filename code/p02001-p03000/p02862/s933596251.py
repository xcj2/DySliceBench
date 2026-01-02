def pow_mod(n, m, mod):
    if m == 0:
        return 1
    if m == 1:
        return n

    res = 1
    if m % 2 == 1:
        res = n

    return ((pow_mod(n * n % mod, m // 2, mod) % mod) * res) % mod


def frac_mod(n, mod):
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i) % mod
    return ans


def cmb_mod(n, r, mod):

    mul1 = frac_mod(n, mod) % mod
    mul2 = pow_mod(frac_mod(r, mod), mod - 2, mod) % mod
    mul3 = pow_mod(frac_mod(n - r, mod), mod - 2, mod) % mod

    return (((mul1 * mul2) % mod) * mul3) % mod


x, y = map(int, input().split())

if (x + y) % 3 != 0 or (2 * x - y) % 3 != 0 or (2 * y - x) % 3 != 0:
    print(0)
    exit(0)


mod = 10 ** 9 + 7
a = (2 * y - x) // 3
b = (2 * x - y) // 3

if a < 0 or b < 0:
    print(0)
    exit(0)

print(cmb_mod(a + b, a, mod))
