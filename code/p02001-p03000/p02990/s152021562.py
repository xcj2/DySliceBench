def build_combinations_counter(N=10**5, p=10**9+7):
    fact = [1, 1]  # fact[n] = (n! mod p)
    factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
    inv = [0, 1]  # mod p におけるnの逆元 n^(-1)
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)
    
    def cmb(n, r, p, fact, factinv):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return fact[n] * factinv[r] * factinv[n-r] % p
    
    import functools
    return functools.partial(cmb, p=p, fact=fact, factinv=factinv)

def resolve():
    N, K = list(map(int, input().split()))
    calc_comb = build_combinations_counter()

    for i in range(1, K+1):
        divs = calc_comb(K-1, i-1)
        reds = calc_comb(i+(N-K-(i-1)), (N-K-(i-1)))
        print((divs*reds)%(10**9+7))
    


if '__main__' == __name__:
    resolve()