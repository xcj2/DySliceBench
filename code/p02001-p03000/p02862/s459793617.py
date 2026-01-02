import sys

mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

def div(a, b):
    return mul(a, power(b, mod-2))

def nCr(n,r):

    if r * 2 > n:
        r = n-r

    now = 1
    for i in range(r):
        now *= n - i
        now *= gdic[r-i]
        now %= mod
    return now


mod = 1000000007
X,Y = map(int,input().split())

a = 0
b = 0

while X > 0 and Y > 0:

    if X > Y:
        a += 1
        X -= 2
        Y -= 1

    else:
        b += 1
        X -= 1
        Y -= 2

"""
factorial = [1]
for n in range(1, a+b):
    factorial.append(factorial[n-1]*n%mod)

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y//2)**2 % mod
    else            : return power(x, y//2)**2 * x % mod

inverseFactorial = [0] * (a+b)
inverseFactorial[a+b-1] = power(factorial[a+b-1], mod-2)
for n in range(a+b-2, -1, -1):
    inverseFactorial[n] = inverseFactorial[n+1] * (n+1) % mod

def combi(n, m):
    return factorial[n] * inverseFactorial[m] * inverseFactorial[n-m] % mod
"""

sys.setrecursionlimit(500000)

gdic = [0]
gyaku = 1
for i in range(min(a,b)):

    i += 2
    gdic.append(gyaku)
    gyaku = mod -gdic[mod % i] * (mod // i) % mod



if X != 0 or Y != 0:
    print (0)

else:
    print (nCr(a+b,a) % mod)
