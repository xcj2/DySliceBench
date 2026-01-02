b, w = [int(i) for i in input().split()]
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

def get_inv(n, p=10**9 + 7):
    inv = [0, 1]
    for i in range(2, n+1):
        inv.append(-(p//i * inv[p%i]) % p)
    return inv

f = fact(b + w + 1)
invf = invfact(b + w + 1, f)

def comb(a, b):
    if a < b:
        return 0
    return f[a] * invf[b] * invf[a-b] % p

P = [[0] * 2 for i in range(b + w + 1)]
B = 0
W = 1
inv_2 = invf[2]

for i in range(1, b + w + 1):
    P[i][B] = P[i - 1][B] + comb(i - 1, b - 1) * inv_2  #i番目になくなってる確率
    P[i][W] = P[i - 1][W] + comb(i - 1, w - 1) * inv_2
    inv_2 = inv_2 * invf[2] % p 
    print((1 - P[i - 1][B] + P[i - 1][W]) * invf[2] % p)
