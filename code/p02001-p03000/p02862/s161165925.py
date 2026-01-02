from functools import reduce
X,Y = (int(x) for x in input().split())
def route(x,y):
    d = min(x,y) - ((x+y)//3)
    if d == 0:
        return 1
    else:
        return (route(x-2,y-1) + route(x-1,y-2))%1000000007
def modmul(a,b):
    return a * b % 1000000007
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
def modinv(a, m):
    g, x, y = xgcd(a, m)
    return x % m
def comb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(modmul, range(n, n - r, -1))
    under = reduce(modmul, range(1,r + 1))
    return over * modinv(under, 1000000007)
if (X+Y) % 3 != 0 or min(X,Y) < (X+Y) // 3:
    print('0')
else:
    d = min(X,Y) - ((X+Y)//3)
    if d == 0:
        print('1')
    else:
        t = (X+Y) // 3
        print((comb(t-1,d)+comb(t-1,d-1))%1000000007)