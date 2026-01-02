import sys
sys.setrecursionlimit(10**6)


def mod_inverse(n, mod=10**9+7):
    return pow(n, mod-2, mod)


def combination(n, k, mod=10**9+7):
    numer = denom = 1
    for i in range(k):
        numer = (numer * (n-i)) % mod
        denom = (denom * (i+1)) % mod
    return (numer * mod_inverse(denom, mod)) % mod


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1) % mod


mod = 10**9+7
N = int(input())
x = [0] + list(map(int, input().split()))
fact = factorial(N-1)

ans = 0
for k in range(2, N):
    ans = (ans + x[k] * (1 - mod_inverse(k)))

for k in range(1, N-1):
    ans = (ans - x[k] * (1 - mod_inverse(N-k))) % mod

ans = ans * fact % mod

ans = (ans + fact * sum((x[N] - x[k]) * mod_inverse(N-k) for k in range(1, N))) % mod

print(ans)
