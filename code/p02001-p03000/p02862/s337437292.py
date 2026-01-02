X, Y = map(int, input().split())

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

def Fac(n, k1, k2):
    t = 1
    kmax = max(k1, k2)
    kmin = min(k1, k2)
    for i in range(1, kmin+1):
        t = t * (kmax+i) * modinv(i, 10**9+7) 
        t = t % (10**9 + 7)
    if n > kmax+kmin:
        for j in range(kmax+kmin+1, n+1):
            t *= j
            t = t % (10**9 + 7)
    return t

s = min(X, Y) - abs(Y - X)

if min(X, Y) - abs(Y - X) < 0:
    print(0)

else:
    if s % 3 != 0:
        ans = 0
    else:
        a = s//3 * 2
        b = abs(Y - X)
        ans = Fac(a+b, a//2, a//2 + b)
        
    print(ans)