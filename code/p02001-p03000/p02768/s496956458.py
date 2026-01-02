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

 # mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


# nCr mod m
# modinvが必要
# rがn/2に近いと非常に重くなる
def combination(n, r, mod=10**9 + 7):
    r = min(r, n - r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i + 1, mod) % mod
    return res
n, a, b = map(int, input().split())


mod = 10**9 + 7
X = combination(n,a)
Y = combination(n,b)
Z = pow_by_binary_exponentiation(2,n,mod) - 1
W = (Z - X - Y) % mod
if W < 0:
    W += mod
print(W % mod)
