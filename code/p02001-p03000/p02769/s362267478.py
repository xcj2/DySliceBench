import math

def modcomb(n, k, mod, fac, ifac):
    x = fac[n]
    y = ifac[n-k] * ifac[k] % mod
    #print(x * y % mod)
    return x * y % mod

def makeTables(n, mod):
    fac = [1, 1]
    ifac = [1, 1]
    inv = [0, 1]

    for i in range(2, n+1):
        fac.append(i * fac[i-1] % mod)
        inv.append(-inv[mod % i] * (mod // i) % mod)
        ifac.append(inv[i] * ifac[i-1] % mod)
    return fac, ifac

def answer(n, k, mod, fac, ifac):
    if k >= n:
        k = n - 1
    ans = 0
    for i in range(k+1):
        c = modcomb(n, i, mod, fac, ifac) * modcomb(n-1, i, mod, fac, ifac) % mod
        ans = (ans + c) % mod

    return ans

n, k = map(int, input().split())
mod = 1000000007

fac, ifac = makeTables(n, mod)
print(answer(n, k, mod, fac, ifac))
