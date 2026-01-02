
N = int(input())
A = list(map(int, input().split()))


def pow(a, b, mod=10 ** 9 + 7):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 == 0:
        return (pow(a, b // 2) ** 2) % mod
    else:
        return (a * pow(a, b // 2) ** 2) % mod


def inv(x, mod=10 ** 9 + 7):
    return pow(x, mod - 2, mod=mod)


def factorize(x):
    ans = {}
    v = 2
    while v * v <= x:
        if x % v == 0:
            ans[v] = 0
            while x % v == 0:
                x //= v
                ans[v] += 1
        v += 1
    if x != 1:
        ans[x] = 1
    return ans


def merge(d, c):
    for k, v in c.items():
        if k not in d:
            d[k] = v
        d[k] = max(d[k], v)


tmp = {}
for v in A:
    merge(tmp, factorize(v))
t = 1
mod = 10 ** 9 + 7
for k, v in tmp.items():
    t *= k ** v
    t %= mod
ans = 0
for a in A:
    ans += t * inv(a)
print(ans % mod)
