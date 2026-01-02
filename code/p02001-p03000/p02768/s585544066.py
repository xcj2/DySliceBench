def solve():

    n, a, b = map(int, input().split())
    mod = 10**9 + 7

    # 繰り返し二乗法
    def modPow(a, n, mod):
        if n == 1:
            return a
        elif n%2 == 1:
            return a * modPow(a, n-1, mod) % mod
        else:
            t = modPow(a, n/2, mod)
            return (t * t) % mod

    def combination(n, a, mod):
        x = 1
        y = 1
        for i in range(a):
            x = x * (n-i)%mod
            y = y * (a-i)%mod

            #x *= (n-i)
            #x %=mod
            #y *= (a-i)
            #y %=mod
        return x * pow(y, mod-2, mod)%mod

    #全ての選び方
    sigma_nCi = pow(2, n, mod)
    # nCa, nCb
    nCa = combination(n, a, mod)
    nCb = combination(n, b, mod)

    ans = sigma_nCi - 1 - nCa - nCb

    #print(Sigma_nCi, nCa, nCb)
    print(ans%mod)

if __name__ == '__main__':
    solve()
