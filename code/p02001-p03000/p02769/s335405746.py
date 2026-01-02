n, k = map(int, input().split())


def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)


def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

def com(n, r, mod):
    r = min(r, n - r)
    if r == 0:
        return 1
    res = ilist[n] * iinvlist[n-r] * iinvlist[r] % mod
    return res


mod = 10**9+7

ilist = [0]
iinvlist = [1]
tmp = 1
for i in range(1, n+1):
    tmp *= i
    tmp %= mod
    ilist.append(tmp)
    iinvlist.append(modinv(tmp, mod))

ans = 0
k = min(n-1, k)
for i in range(k+1):
    tmp = com(n, i, mod)
    tmp *= com(n-1, i, mod)
    ans += tmp
    ans %= mod


print(ans)