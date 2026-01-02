n, a, b = map(int, input().split())

mod = 10 ** 9 + 7

def mod_pow(x:int, y:int):
    if y % 2 == 0:
        return (mod_pow(x, y // 2) ** 2) % mod
    elif y == 1:
        return x % mod
    else:
        return ((mod_pow(x, y // 2) ** 2) * x) % mod

def mod_inverse(a:int):
    return (mod_pow(a, mod - 2)) % mod

def mod_nCr(n:int, r:int):
    num, den = 1, 1
    for i in range(r):
        num = (num * (n - i)) % mod
        den = (den * (r - i)) % mod
    return (num * mod_inverse(den)) % mod

ans = (mod_pow(2, n) - mod_nCr(n, a) - mod_nCr(n, b) - 1)  % mod
print(ans)