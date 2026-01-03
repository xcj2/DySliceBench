MOD = 1000000007
lim = 200000
inv_t = [-1 for i in range(lim+1)]
factrial = [-1 for i in range(lim+1)]
factrial_inv = [-1 for i in range(lim+1)]


def set_inv(max=lim):
    inv_t[0] = 0
    for i in range(1, max):
        inv_t[i] == mod_inv(i)


def mod_inv(x, mod=MOD):
    y, u, v, _x = mod, 1, 0, x
    while y:
        t = _x//y
        _x -= t*y
        _x, y = y, _x
        u -= t*v
        u, v = v, u
    u %= mod
    if u < 0:
        u += mod
    return u


def mod_pow(a, n, mod=MOD):
    res = 1
    while n:
        if n & 1:
            res = res*a % mod
        a = a*a % mod
        n >>= 1
    return res


def set_factrial(max=lim, mod=MOD):
    c = 1
    factrial[0] = factrial_inv[0] = 1
    for i in range(1, max):
        c *= i
        c %= mod
        factrial[i] = c
        factrial_inv[i] = mod_inv(c, mod)


def comb(a, b, mod=MOD):
    if factrial[0] == -1:
        set_factrial()
    return (factrial[a]*factrial_inv[b]*factrial_inv[a-b]) % mod


N = n = int(input())
s = [input() for i in range(2)]

ret = []
i = 0
while i < N:
    if s[0][i] == s[1][i]:
        ret.append(1)
        i += 1
    else:
        ret.append(2)
        i += 2
ans = 3*ret[0]
for i in range(1, len(ret)):
    if ret[i-1] == 1 and ret[i] == 1:
        ans *= 2
    elif ret[i-1] == 1 and ret[i] == 2:
        ans *= 2
    elif ret[i-1] == 2 and ret[i] == 1:
        ans *= 1
    elif ret[i-1] == 2 and ret[i] == 2:
        ans *= 3
    ans %= MOD

print(ans)
# print(ret)
