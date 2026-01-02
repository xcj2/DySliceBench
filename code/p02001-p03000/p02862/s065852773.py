def mod_pow(a, x, p):
    res = 1
    while x > 0:
        if x % 2 != 0:
            res = (res * a) % p
        a = (a * a) % p
        x //= 2
    return res


def mod_inv(a, p):
    return mod_pow(a, p-2, p)


def mod_binomial(n, k, p):
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n-i)) % p

    denominator = 1
    for i in range(1, k+1):
        denominator = (denominator * i) % p

    return (numerator * mod_inv(denominator, p)) % p


X, Y = map(int, input().split())

a = (2*Y-X) / 3
b = (2*X-Y) / 3

if a >= 0 and b >= 0 and a == int(a) and b == int(b):
    a = int(a)
    b = int(b)

    print(mod_binomial(a+b, a, 10**9+7))
else:
    print(0)
