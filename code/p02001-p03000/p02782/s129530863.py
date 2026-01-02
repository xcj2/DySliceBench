mod = 10 ** 9 + 7


def pow(a, b, mod):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b % 2 == 0:
        return (pow(a, b // 2, mod) ** 2) % mod
    else:
        return (a * pow(a, b // 2, mod) ** 2) % mod


def inv(x, mod):
    return pow(x, mod - 2, mod)


MAX = 2 * 10 ** 6 + 3
l = [1] * MAX
for i in range(1, MAX):
    l[i] = (l[i - 1] * i) % mod


def f(r, c):
    return (l[r + c] * inv(l[r], mod) * inv(l[c], mod)) % mod


def g(r, c):
    if r < 0 or c < 0:
        return 0
    ans = f(r+1, c+1) - 1 + mod
    return ans % mod


r1, c1, r2, c2 = map(int, input().split())
print(((g(r2, c2) - g(r2, c1 - 1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)) % mod + mod) % mod)
