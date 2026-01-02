def sq(a, b, mod):  # aのb乗を剰余,kは初期値#20191116-D-Knight
    if b == 0:
        return 1
    elif b % 2 == 0:
        return sq(a, b // 2, mod)**2 % mod
    else:
        return sq(a, b - 1, mod) * a % mod


def nCk(n, k, mod=10 ** 9 + 7):
    x = max(k, n - k)
    y = min(k, n - k)
    kkai = 1
    for i in range(2, y + 1):
        kkai = (kkai * i) % mod
    nkkai = 1
    for i in range(x + 1, n + 1):
        nkkai = (nkkai * i) % mod
    answer = sq(kkai, mod - 2, mod) * nkkai % mod
    return answer

mod = 10**9+7
n, a, b = map(int, input().split())

def modpow(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = res*x % (10**9+7)
        x = x*x%(10**9+7)
        y >>= 1
        y = int(y)
    return res
ans = 0
ans -= nCk(n, b)
ans -= nCk(n, a)
ans -= 1
ans += modpow(2, n)
print((ans+10**9+7)%(10**9+7))