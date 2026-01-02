mo = 10**9 + 7
def fac(x):
    ans = 1
    for i in range(1,x+1):
        ans *= i
        ans %= mo
    return ans

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

def f():
    x,y = [int(s) for s in input().split()]
    if x > (y*2):
        return 0
    if y > (x*2):
        return 0
    if (2*x-y)%3:
        return 0
    if (2*y-x)%3:
        return 0
    a = (2*x-y)//3
    b = (2*y-x)//3
    if a==0 or b==0:
        return 1
    ar = modinv(fac(a),mo)
    br = modinv(fac(b),mo)
    ans = (((fac(a+b) * ar)%mo)*br)%mo
    return ans


print(f())
