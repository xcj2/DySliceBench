def main():
    n, m, k = map(int, input().split())
    mod = 998244353
    if m == 1:
        if k == n-1 or n == 1:
            print(1)
        else:
            print(0)
        return
        
    ans = 0
    m1 = [None]*n
    kai = [None]*n
    mi = 1
    ki = 1
    for i in range(n):
        m1[i] = mi
        mi *= m-1
        mi %= mod
        kai[i] = ki
        ki *= (i+1)
        ki %= mod
        
    def comb(a, b):
        return kai[a]*fermat(kai[a-b]*kai[b], mod)
        
    def fermat(x, p):
        """
        1/x (mod p) を返す
            x**(p-1) ≡ 1    [if gcd(x, p) == 1]
            x**(p-2) ≡ 1/x
            繰返し二乗法 
                ex: x**50  = (x**25)**2
                    x**25  = (x**12)**2 * x
                    x**12  = (x**6)**2
                    x**6   = (x**3)**2
        """
        times = []
        mod = p
        p -= 2
        while p > 1:
            times.append(p%2)
            p //= 2
        x %= mod
        out = x
        for i in times[::-1]:
            if i:
                out = (x*pow(out, 2, mod))%mod
            else:
                out = pow(out, 2, mod)
        return out
               
    for i in range(k+1):
        ans += m*comb(n-1, i)*m1[n-i-1]
        ans %= mod
    print(ans)

    

if __name__ == "__main__":
    main()