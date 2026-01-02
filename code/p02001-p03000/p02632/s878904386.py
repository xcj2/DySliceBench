k = int(input())
s = input()

n = len(s)
mod = 10**9+7


def framod(n, mod, a=1):
    for i in range(1, n+1):
        a = a * i % mod
    return a


def power(n, r, mod):
    if r == 0:
        return 1
    if r % 2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r % 2 == 1:
        return n * power(n, r-1, mod) % mod


def comb(n, k, mod):
    a = framod(n, mod)
    b = framod(k, mod)
    c = framod(n-k, mod)
    return (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod


com = [1]*(k+1)
for i in range(k):
    com[i+1] = com[i]*(n+i)*pow(i+1, mod-2, mod) % mod

a25 = [1]*(k+1)
for i in range(k):
    a25[i+1] = a25[i]*25 % mod
a26 = [1]*(k+1)
for i in range(k):
    a26[i+1] = a26[i]*26 % mod
num = 0
for i in range(0, k+1):
    num = (num+com[i]*a25[i] % mod * a26[k-i]) % mod
print(num)
