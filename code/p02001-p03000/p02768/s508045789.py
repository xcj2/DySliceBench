n, a, b = map(int, input().split())
mod = 10**9+7


def binary(n):
    return bin(n)[2:]


# a^x mod n : ans = pow_by_binary_exponentiation(2, 1000, 10**9+7)
def pow_by_binary_exponentiation(a, x, n):
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % n
        if x[i] == 1:
            y = (y * a) % n
    return y


def combination(n, r, mod=10**9+7):
    n1, r = n+1, min(r, n-r)
    numer = denom = 1
    for i in range(1, r+1):
        numer = numer * (n1-i) % mod
        denom = denom * i % mod
    return numer * pow(denom, mod-2, mod) % mod


ac = combination(n, a, mod)
bc = combination(n, b, mod)
ans = pow_by_binary_exponentiation(2, n, mod)
print(((ans - ac - bc - 1) % mod)//1)
