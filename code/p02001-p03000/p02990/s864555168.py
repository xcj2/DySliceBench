n, k = [int(i) for i in input().split()]
p = 10 ** 9 + 7

def fact(n, p=10**9 + 7):
    f = [1]
    for i in range(1, n+1):
        f.append(f[-1]*i%p)
    return f

def invfact(n, f, p=10**9 + 7):
    inv = [pow(f[n], p-2, p)]
    for i in range(n, 0, -1):
        inv.append(inv[-1]*i%p)
    return inv[::-1]

f = fact(n)
invf = invfact(n, f)

def comb(a, b, p=10 ** 9 + 7):
    if a < b:
        return 0
    if a < 0 or b < 0:
        return 0
    return f[a] * invf[b] * invf[a-b] % p

b = k
r = n - k

for i in range(1, k + 1):
    print(comb(r + 1, i) * comb(b - 1, i - 1) % p)