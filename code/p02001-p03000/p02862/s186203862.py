def solve():
    mod = 10 ** 9 + 7
    fac, finv, inv = COMinit(10 ** 6, mod)

    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    
    ans = 0
    for one_cnt in range(10 ** 6):
        x1 = one_cnt * 2
        y1 = one_cnt * 1
        remain_x = X - x1
        remain_y = Y - y1
        if remain_x * 2 != remain_y or remain_x < 0 or remain_y < 0:
            continue
        two_cnt = remain_x
        ans += COM(one_cnt+two_cnt, one_cnt,mod,fac,finv,inv)
    
    print(ans)

def n_combination(n, r, mod):
    numer_sum = 1
    denom_sum = 1
    for i in range(r):
        numer_sum *= n - i
        numer_sum % mod
        denom_sum *= r - i
        numer_sum % mod
    
    return numer_sum * modinv(denom_sum, mod) % mod

def modinv(a, mod):
    return pow(a, mod-2, mod)
    
def COMinit(N, mod):
    fac = [0] * N
    finv = [0] * N
    inv = [0] * N

    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1

    for i in range(2, N):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod
    
    return fac, finv, inv

def COM(n, r, mod, fac, finv, inv):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n-r] % mod) % mod

if __name__ == '__main__':
    solve()