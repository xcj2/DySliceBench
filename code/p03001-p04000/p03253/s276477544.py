def prime_factor(n):
    ret, p = {}, 2
    while p*p <= n:
        while n % p == 0:
            ret[p] = ret.get(p, 0) + 1
            n //= p
        p += 1
    if n != 1: ret[n] = 1
    return ret


def mod_inverse(x, mod):
    return pow(x, mod-2, mod)


def mod_comb(n, k, mod):
    numer, denom = 1, 1
    for i in range(k):
        numer = numer * ((n-i) % mod) % mod
        denom = denom * ((i+1) % mod) % mod

    return numer * mod_inverse(denom, mod) % mod


def main():
    n, m = map(int, input().split())
    prime = prime_factor(m)
    mod = 1000000007
    ans = 1
    for (p, e) in prime.items():
        ans = ans * mod_comb(n+e-1, e, mod) % mod

    print(ans)

main()