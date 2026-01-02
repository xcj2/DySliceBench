n, a, b = map(int, input().split())
mod = 10**9+7


def extgcd(a, b):
    r = [1, 0, a]
    w = [0, 1, b]
    while w[2] != 1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0], r[1]-q*w[1], r[2]-q*w[2]]
        r = r2
        w = w2
    # [x,y]
    return [w[0], w[1]]


def mod_inv(a, m):
    x = extgcd(a, m)[0]
    return (m+x % m) % m


def comb(n, r, mod):
    u = 1
    d = 1
    for i in range(r):
        u *= n-i
        d *= i+1
        if u >= mod:
            u %= mod
        if d >= mod:
            d %= mod
    return u*mod_inv(d, mod)


def binary(n):
    return bin(n)[2:]


def pow_by_binary_exponentiation(a, x, n):  # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y


ac = comb(n, a, mod)
bc = comb(n, b, mod)
ans = pow_by_binary_exponentiation(2, n, mod)
print(((ans - ac - bc - 1) % mod)//1)
