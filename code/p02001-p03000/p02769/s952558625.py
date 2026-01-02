n, k = map(int, input().split())

MOD = 10**9 + 7

def cmb(n, r, mod=10**9 + 7):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod

def make_table(n, mod=10**9 + 7):
    # 元テーブル
    g1 = [0] * (n + 1)
    g1[0] = 1
    g1[1] = 1

    # 逆元テーブル
    g2 = [0] * (n + 1)
    g2[0] = 1
    g2[1] = 1

    # 逆元計算用テーブル
    inverse = [0] * (n + 1)
    inverse[0] = 0
    inverse[1] = 1

    for i in range(2, n + 1):
        g1[i] = (g1[i - 1] * i) % mod
        inverse[i] = (-inverse[mod % i] * (mod // i)) % mod
        g2[i] = (g2[i - 1] * inverse[i]) % mod

    return tuple(g1), tuple(g2), tuple(inverse)

g1, g2, inverse = make_table(2*n)

# n! (MOD p)
def factorial_mod(n, p = MOD):
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
        tmp %= p
    return tmp

if n-1 <= k:
    print(cmb(2*n-1, n-1))
else:
    ans = 1
    for n_empty in range(1, k+1):
        ans += cmb(n, n_empty) * cmb(n-1, n-1-n_empty)
        ans %= MOD
    print(ans)