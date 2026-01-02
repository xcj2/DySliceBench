x, y = map(int, input().split())
if (x + y) % 3 != 0:
    print(0)
    exit(0)
row = (x + y) // 3
mod = 10 ** 9 + 7
if x < row or x > row * 2:
    print(0)
    exit(0)
x = x - row

def pow_mod(a, x, mod):
    if x == 0:
        return 1 % mod
    if x == 1:
        return a % mod
    half = pow_mod(a, x // 2, mod)
    half = half * half % mod
    if x % 2 == 1:
        half = half * a % mod
    return half

def rev(i, mod):
    return pow_mod(i, mod - 2, mod)

def calc(n, m, mod):
    if n == m or m == 0:
        return 1
    if n - m < m:
        m = n - m
    ans = 1
    for i in range(1, m + 1):
        f1 = ans * (n-i+1) * rev(i, mod) % mod
        ans = f1
    return ans


print(calc(row, x, mod))
