import math

def prime_factorize(n):
    ret = []
    # 小さい素数から順に試し割りしていく
    for i in range(2, int(math.sqrt(n))+1):
        if n % i != 0:
            continue
        e = 0
        while n % i == 0:
            e += 1
            n //= i
        ret += [(i, e)]

    if n != 1:
        ret += [(n, 1)]

    return ret


def extgcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        g = b
    return x, y, g


def modinv(a, m):
    x, y, g = extgcd(a, m)
    if g != 1:
        print ("[+]Inverse does not exist.")
    else:
        return ((m + x) % m) % m


def mod_comb(n, r, mod):
    ans_mul, ans_div = 1, 1

    for i in range(r):
        ans_mul *= (n-i)
        ans_div *= (i+1)
        ans_mul %= mod
        ans_div %= mod

    return ans_mul * modinv(ans_div, mod) % mod


def main():
    N, M = map(int, input().split())
    v = prime_factorize(M)
    MOD = int(10**9+7)
    ans = 1

    for i in v:
        ans *= mod_comb(N+i[1]-1, i[1], MOD)
        ans %= MOD
    print (ans)

main()
