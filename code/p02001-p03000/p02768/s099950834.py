# mod. m での a の逆元 a^{-1} を計算する
# b * a^{-1} (mod m)を計算したい場合はb * modinv(a, m) % m
def modinv(a, m):
    b = m
    u = 1
    v = 0
    while b:
        t = int(a / b)
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u


# 高速な累乗計算
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
    
    
# 途中計算でmodを計算する高速な累乗計算
def pow_k_mod(x, n, m):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
            K %= m
        x *= x
        x %= m
        n //= 2

    return (K * x) % m
    
n, a, b = map(int, input().rstrip().split())

max_num = pow_k_mod(2, n, int(1e9+7)) - 1
a = max(a, n - a)
b = max(b, n - b)

num_a = 1
for i in range(a+1, n+1):
    num_a *= i
    num_a %= int(1e9+7)
for i in range(1, n - a + 1):
    num_a = (num_a * modinv(i, int(1e9+7))) % int(1e9+7)
    
num_b = 1
for i in range(b+1, n+1):
    num_b *= i
    num_b %= int(1e9+7)
for i in range(1, n - b + 1):
    num_b = (num_b * modinv(i, int(1e9+7))) % int(1e9+7)
    
print((max_num - num_a - num_b) % int(1e9+7))