def cmb(n, k, mod):
    numerator = 1
    for i in range(k):
        numerator = (numerator * (n-i)) % mod

    denominator = 1
    for i in range(1, k+1):
        denominator = (denominator * i) % mod

    return (numerator * pow(denominator, mod-2, mod)) % mod


def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x


def myPow(x, n, m):
    if(n == 0):
        return 1
    if(n % 2 == 0):
        return myPow(x * x % m, n / 2, m)
    else:
        return x * myPow(x, n - 1, m) % m


n, a, b = map(int, input().split())
mod = 10**9 + 7
print((myPow(2, n, mod) - cmb(n, a, mod) - cmb(n, b, mod) - 1) % mod)
