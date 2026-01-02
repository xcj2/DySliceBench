def main():
    n, m, k = map(int, input().split())
    mod = 998244353
    kai = [None]*n
    m1 = [None]*n
    num = 1
    ki = 1
    for i in range(n):
        m1[i] = num
        num *= m-1
        num %= mod
        kai[i] = ki
        ki *= i+1
        ki %= mod
    
    def comb(a, b):
        return kai[a]*fermat(kai[b]*kai[a-b], mod)
        
    ans = 0
    for i in range(k+1):
        ans += m*m1[n-1-i]*comb(n-1, i)
        ans %= mod
    print(ans)
        
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

if __name__ == "__main__":
    main()