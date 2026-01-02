n,k = map(int, input().split())

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def comb(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

def nHr(n,r):
    return comb(n+r-1,r)

def getR(i):
    split=i+1
    must1=i-1
    balls=n-k-must1
    if balls<0:
        return 0
    return nHr(split,balls)

def getB(i):
    split=i
    must1=i
    balls=k-must1
    if balls<0:
        return 0
    return nHr(split,balls)

for i in range(1,k+1):
    ans = (getR(i)*getB(i)) % (10**9+7)
    print(ans)