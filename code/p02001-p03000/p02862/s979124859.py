def kaijou(n, r, mo):
    c = 1
    for i in range(r+1, n+1):
        c *= i
        c %= mo
    return c

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def invmod(a, m):
    g, x, y = xgcd(a, m)
    return x % m

def kaijou_inv(ans, n, mo):
    for i in range(1,n+1):
        ans *= invmod(i, mo)
        ans %= mo
    return ans


x, y = map(int, input().split())
mo = 10**9 + 7
if (x+y) % 3 != 0:
    print(0)
else:
    a = (2*x-y) // 3
    b = (2*y-x) // 3
    if a<0 or b<0:
        print(0)
    else:
        te = kaijou(a+b, max(a, b), mo)
        tem = kaijou_inv(te, min(a,b), mo)
        print(tem)