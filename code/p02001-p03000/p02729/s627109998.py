def binary(n):
    return bin(n)[2:]

def pow_w_mod(a, x, mod):  # a^x mod n
    x = [int(b) for b in binary(x)]
    y = a
    for i in range(1, len(x)):
        y = (y**2) % mod
        if x[i] == 1:
            y = (y * a) % mod
    return y
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def combination(n, r, mod=10**9 + 7):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res

n, m = map(int, input().split())
#a = combination(n+m, 2, mod=10**9 + 7)

if n < 2:
    b = 0 
else:
    b = combination(n, 2, mod=10**9 + 7)

if m < 2:
    c = 0
else:
    c = combination(m, 2, mod=10**9 + 7)
print(b+c)