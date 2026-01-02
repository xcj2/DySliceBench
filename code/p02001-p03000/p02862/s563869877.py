import sys

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

def comb_num_mod(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

def solver(x, y):


    if (x, y) == (0, 0):
        return 0
    if (x+y)%3 != 0:
        return 0
    k = (x+y)//3
    (xi, yi) = (k, 2*k)
    for i in range(k+1):
        if (xi, yi) == (x, y):
            return comb_num_mod(k, i) 
        else:
            (xi, yi) = (xi+1, yi-1)
    return 0

x, y = map(int, input().split())
res = solver(x, y)
print(res)