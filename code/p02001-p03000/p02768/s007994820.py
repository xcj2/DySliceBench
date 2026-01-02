#d
n,a,b = map(int,input().split())

def power(x, n, mod):
    """
    x**n mod in  O(log n)
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
    return K * x % mod
 
def nCrMOD(a,b,m):
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

m=10**9+7

ans = power(2,n,m) -1 - nCrMOD(n,a,m) -nCrMOD(n,b,m)
print(ans%m)