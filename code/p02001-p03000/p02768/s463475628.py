n, a, b = map(int, input().split())
mod = 10**9 + 7

def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n % 2 != 0:
            K = K * x % mod
            x = x ** 2 % mod
            n = (n - 1) // 2
        else:
            x = x ** 2 % mod
            n = n // 2

    return K * x % mod# 指数を割り続け n が 1 に至ったら終了

def modc(a,b,m):
    c = 1
    for i in range(b):
        c = c * (a - i) % m
        c = c * modinv(i + 1,m) % m
    return c

def egcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)

def modinv(a, m):
    (inv, q, gcd_val) = egcd(a, m)
    return inv % m

ans = pow_k(2, n) - 1
ans -= modc(n, a, mod) + modc(n, b, mod)
ans = ans % mod
print(ans)