mod = int(1e9) + 7
n, a, b = map(int, input().split())

def aaa(base, n):
#     base = 2
    ans = 1
    nn = n
    while True:
    #     print(base, nn)
        if nn == 0:
            break
        if nn % 2 == 0:
            base = base ** 2
            base = base % mod
            nn /= 2
        else:
            ans *= base
            ans = ans % mod
            nn -= 1
    return ans

xn = aaa(2, n)

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def div(a, b):
    return mul(a, power(b, mod-2))


def fac(start, length, mod):
    x = 1
    for k in range(start, start + length):
        x *= k
        x %= mod
    return x

aa = fac(n - a + 1 , a, mod)
aaa = fac(1, a, mod)
xa = div(aa, aaa)
if aa == 0:
    if aaa == 0:
        xa = 1


bb = fac(n - b + 1 , b, mod)
bbb = fac(1, b, mod)
xb = div(bb, bbb)
if bb == 0:
    if bbb == 0:
        xb = 1
        

x = xn - xa - xb - 1
x = x % mod
if x < 0:
    x += mod
print(x)
