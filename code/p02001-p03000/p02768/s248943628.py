def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def comb(n, r, p):
    ret = 1
    while 1:
        if (r == 0):
            break
        N = n % p
        R = r % p
        if N < R:
            return 0
        for i in range(R):
            ret = ret * (N-i) % p
        imul = 1
        for i in range(R):
            imul = imul * (i+1) % p
        ret = ret * modinv(imul, p) % p
        n //= p
        r //= p
    return ret

mod = 10 ** 9 + 7
N, A, B = map(int, input().split())
tmp = (2 ** N - 1) % mod 
a = comb(N, A, mod)
b = comb(N, B, mod)
print(((tmp + mod) - a - b ) % mod)