h, w, a, b = [int(i) for i in input().split()]

p = 10 ** 9 + 7

ans = 0
c = h-a-1

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

f = fact(h+w-2)
invf = invfact(h+w-2, f)

def comb(a, b):
    return f[a] * invf[b] * invf[a-b] % p

for x in range(b, w):
    ans = (ans + (comb(c+x, min(x, c)) * comb(a-1+w-x-1, min(a-1, w-x-1)) % p)) % p

print(ans)