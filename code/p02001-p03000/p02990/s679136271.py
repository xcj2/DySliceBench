import sys
inputs = sys.stdin.readlines()

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def modinv(a, mod):
    g, x, y = xgcd(a, mod)
    assert g == 1, 'modular inverse does not exist'
    return x % mod

factorials = [1]
def factorial(n, mod):
    # n! % mod
    assert n >= 0, 'Argument Error! n is "0 <= n".'
    if len(factorials) < n+1:
        for i in range(len(factorials), n+1):
            factorials.append(factorials[-1]*i % mod)
    return factorials[n]

def perm(n, r, mod):
    # nPr % mod
    assert n >= 0, 'Argument Error! n is "0 <= n".'
    assert n >= r >= 0, 'Argument Error! r is "0 <= r <= n".'
    return factorial(n, mod) * modinv(factorial(n-r, mod), mod) % mod

def comb(n, r, mod):
    # nCr % mod
    assert n >= 0, 'Argument Error! n is "0 <= n".'
    assert n >= r >= 0, 'Argument Error! r is "0 <= r <= n".'
    
    return perm(n, r, mod) * modinv(factorial(r, mod), mod) % mod

n, k = map(int, inputs[0].split())
MOD = 10 ** 9 + 7

for i in range(1, k+1):
    try:
        print(comb(n-k+1, i, MOD)*comb(k-1, i-1, MOD) % MOD)
    except:
        print(0)