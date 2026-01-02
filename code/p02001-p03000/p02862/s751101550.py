X, Y = map(int, input().split())
MOD = 10 ** 9 + 7

def createFacArr(n, mod):
    fac = [0] * n
    finv = [0] * n
    inv = [0] * n
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, n):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod
    return fac, finv, inv

def comb(n ,k, mod, fac, finv, inv):
    '''
    二項係数の計算
    '''
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

def main():
    if (X + Y) % 3 != 0:
        return 0
    # 移動回数を求める
    m = (2 * X - Y) // 3
    n = X - 2 * m
    fac, finv, inv = createFacArr(10**6*2, MOD)
    return comb(m+n, n, MOD, fac, finv, inv)

print(main())
