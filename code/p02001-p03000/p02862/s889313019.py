a, b = map(int, input().split())

def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def power(x, y, mod):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2, mod)**2 % mod
    else            : return power(x, y//2, mod)**2 * x % mod

def comb(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod

import math
if (2 * a - b) % 3 != 0 or (2 * b - a) % 3 != 0:
    print(0)
else:
    d = (2 * b - a) // 3
    c = (2 * a - b) // 3
    if c < 0 or d < 0:
        print(0)
    else:
        print(comb(c+d, c, 10 ** 9 + 7))
