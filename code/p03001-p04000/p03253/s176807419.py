MOD = int(1e9+7)
f = {}
f[0] = 1
for i in range(1, 100100):
    f[i] = f[i - 1] * i
    f[i] %= MOD

def mod_pow(x, y):
    if y == 0:
        return 1
    res = mod_pow(x * x % MOD, y // 2)
    if y & 1 == 1:
        res = res * x
    return res

def inverse(x):
    return mod_pow(x, MOD - 2)

def cmb(n, r):
    return f[n] * inverse(f[r] * f[n - r] % MOD)

n, m = map(int, input().split())
ans = 1
t = 2
while m >= t ** 2:
    cnt = 0
    while m % t == 0:
        m //= t
        cnt += 1
    if cnt > 0:
        ans *= cmb(n + cnt - 1, cnt) % MOD
        ans %= MOD
    t += 1
if m > 1:
    ans *= n
    ans %= MOD
print(ans)