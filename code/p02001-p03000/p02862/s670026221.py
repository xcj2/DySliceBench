import sys
input = sys.stdin.readline

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

def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

X, Y = [int(x) for x in input().strip().split()]
p = (X, 2 * X)
n1 = X
n2 = 0
f = True
while p != (X, Y):
    n1 -= 2
    n2 += 1
    p = (n1 + 2 * n2, 2 * n1 + n2)
    if p[1] <= 0:
        f = False
        break

if n1 < 0 or n2 < 0:
    print(0)
else:
    print(combination(n1 + n2, n1) % (10 ** 9 + 7))