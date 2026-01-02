n = int(input())
if n == 1:
    print(1)
    exit()
if n == 2:
    print(3)
    exit()
n *= 2
ans = n*2

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
        return float("INF")
    else:
        return x % m
def calc(b1,m1,b2,m2):
    p = modinv(m1,m2)
    if p == float("INF"):
        return float("INF")
    d = 1
    if (b2-b1)%d:
        return float("INF")
    tmp = (b2-b1)*p%m2
    m = m1*m2//d
    tmp = (b2-b1)//d*p%(m2//d)
    r = (b1+m1*tmp)%m
    return r

for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        ans = min(ans,calc(0,i,n//i-1,n//i))
        if i != 1:
            ans = min(ans,calc(0,n//i,i-1,i))
print(ans)