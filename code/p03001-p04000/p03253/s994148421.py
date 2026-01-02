
import math
def primes(x):
    if x < 2:
        return []
    ps = [i for i in range(x)]
    ps[1] = 0
    for p in ps:
        if p > math.sqrt(x): break
        if p == 0: continue
        for np in range(2 * p, x, p):
            ps[np] = 0
    return [p for p in ps if p != 0]


def prime_factors(ps, x):
    pfs = []
    for p in ps:
        i = 0
        while x % p == 0:
            x = x // p
            i += 1
        if i != 0:
            pfs.append((p,i))
    return pfs


def mod_comb(a,b,mod):
    #print(a,b)
    if a-b < b: return mod_comb(a,a-b,mod)
    ans_mul = 1
    ans_div = 1
    for i in range(b):
        ans_mul *= a-i
        ans_div *= i+1
        ans_mul %= mod
        ans_div %= mod
    return (ans_mul * modpow(ans_div, mod-2, mod)) % mod

def modpow(a,b,mod):
    if b == 0: return 1
    if b % 2 == 0:
        h = modpow(a, b//2, mod)
        return (h * h) % mod
    else:
        return (a * modpow(a, b-1, mod)) % mod

if __name__ == '__main__':
    MOD = 1000000007
    words = lambda t : list(map(t, input().split()))
    n,m = words(int)
    ans = 1
    for i in range(2,m):
        if i*i > m:
            break
        cnt = 0
        while m % i == 0:
            m = m // i
            cnt += 1
        #print(i, cnt)
        if cnt != 0:
            ans *= mod_comb(n + cnt - 1,n-1,MOD)
            ans %= MOD
    if m != 1:
        ans *= mod_comb(n,n-1,MOD)
        ans %= MOD

    print(ans)
