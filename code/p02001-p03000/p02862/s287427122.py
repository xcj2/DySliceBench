def extgcd(a, b):
    if b == 0:
        return [1, 0, a]
    x, y, g = extgcd(b, a % b)
    return [y, x - a//b * y, g]


def mod_inverse(a, m):
    x, y, _ = extgcd(a, m)
    return (m + x % m) % m


def mod_comb(n, k, mod):
    mul, div = 1, 1
    for i in range(k):
        mul *= (n-i)
        div *= (i+1)
        mul %= mod
        div %= mod
    return mul * mod_inverse(div, mod) % mod


X, Y = map(int, input().split())

if (X + Y) % 3 != 0:
    print(0)
    exit(0)

al = (X + Y) // 3
ch = (2 * Y - X) // 3
if ch < 0 or al - ch < 0:
    print(0)
    exit(0)
print(mod_comb(al, ch, int(1e9+7)))