n = int(input())
A = [int(i) for i in input().split()]

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

def get_inv(n, f, invf, p=10**9 + 7):
    inv = [0]
    for i in range(n):
        inv.append(invf[i+1] * f[i] % p)
    return inv

f = fact(30+10**5)
invf = invfact(30+10**5, f)
inv = get_inv(30+10**5, f, invf)

def comb(a, b):
    return f[a] * invf[b] * invf[a-b] % p

csum = [0]

for i in range(1, n+1):
    csum.append((csum[-1] + inv[i]) % p)

ans = 0
for i, a in enumerate(A):
    ans += (csum[i+1] + csum[n-i] - csum[1] + p) % p * a
    ans %= p

print(ans * f[n] % p)