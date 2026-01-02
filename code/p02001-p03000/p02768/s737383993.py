MOD = 10**9 + 7
def MOD_pow(a, n):
    res = 1
    while n > 0:
        if (n & 1):
            res = res * a % MOD
        a = a * a % MOD
        n = n // 2
    return res
def MOD_perm(n, r):
    rtn = 1
    for _ in range(r):
        rtn *= n
        rtn %= MOD
        n -= 1
    return rtn
def MOD_inv(a):
    b = MOD
    u = 1
    v = 0
    while b > 0:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u = u % MOD
    if u < 0:
        u += MOD
    return u
def cmb(n, r):
    return MOD_perm(n, r) * MOD_inv(MOD_perm(r, r)) % MOD

def main():
    n, a, b = map(int, input().split())
    ans = MOD_pow(2, n) - cmb(n, a) - cmb(n, b) - 1
    while ans < 0:
        ans += MOD
    print(ans)

if __name__ == "__main__":
    main()