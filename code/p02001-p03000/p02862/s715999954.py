def multiple_of_n(x, y, n=3):
    return (x - y) % n == 0

def combination(g1, g2, inverse, n, r, mod):
    if (r < 0 or r > n):
        return 0
    r = min([r, n - r])
    return g1[n] * g2[r] * g2[n - r] % mod

def make_inv(mod, N):
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]
    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((- inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)
    return g1, g2, inverse

mod = 10 ** 9 + 7

x, y = map(int, input().split())
if multiple_of_n(2 * x, y) and multiple_of_n(2 * y, x):
    vertical = (2 * y - x) // 3
    horizontal = (2 * x - y) // 3
    total = vertical + horizontal
    g1, g2, inverse = make_inv(mod, total)
    print(combination(g1, g2, inverse, total, horizontal, mod))
else:
    print(0)