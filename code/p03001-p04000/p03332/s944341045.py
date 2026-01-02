class Factorial():
    def __init__(self, n, mod):
        self.mod = mod
        self.fct = [0 for _ in range(n + 1)]
        self.inv = [0 for _ in range(n + 1)]
        self.fct[0] = 1
        self.inv[0] = 1
        for i in range(n):
            self.fct[i + 1] = self.fct[i] * (i + 1) % mod
        self.inv[n] = pow(self.fct[n], mod - 2, mod)
        for i in range(n)[::-1]:
            self.inv[i] = self.inv[i + 1] * (i + 1) % mod

    def comb(self, m, k):
        if m < k: return 0
        return self.fct[m] * self.inv[k] * self.inv[m - k] % self.mod

def ex_euclid(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1
    while c1:
        a0, a1 = a1, a0 - c0 // c1 * a1
        b0, b1 = b1, b0 - c0 // c1 * b1
        c0, c1 = c1, c0 % c1
    return c0, a0, b0

MOD = 998244353
N, A, B, K =map(int,input().split())

f = Factorial(N, MOD)
c, a, b = ex_euclid(A, B)

if K == 0:
    print(1)

elif K % c != 0:
    print(0)

else:
    lo = -10**18
    hi = 10**18
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if a * K // c + mid * B // c >= 0:
            hi = mid
        else:
            lo = mid
    x0 = a * K // c + hi * B // c

    lo = -10**18
    hi = 10**18
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if b * K // c - mid * A // c >= 0:
            lo = mid
        else:
            hi = mid
    y0 = b * K // c - lo * A // c

    res = 0
    x = x0
    y = (K - A * x0) // B

    while True:
        res += f.comb(N, x) * f.comb(N, y)
        res %= MOD
        if y == y0:
            break
        x += B // c
        y -= A // c

    print(res)