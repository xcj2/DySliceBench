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

x, y = map(int, input().split())

if (x+y) % 3 != 0:
    print(0)
    exit()

if x/2 > y or y/2 > x:
    print(0)
    exit()

maxi = max(x, y)
mini = min(x, y)

tate = 0
yoko = 0
while mini/2 != maxi:
    tate += 1
    maxi -= 2
    mini -= 1
yoko = maxi

print(modc(yoko+tate, yoko, 10**9+7))