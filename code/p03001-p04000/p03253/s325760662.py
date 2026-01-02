import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from collections import Counter


class Combination:
    def __init__(self, n):
        self.fac = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = (self.fac[i - 1] * i) % mod
        self.invmod = [1] * (n + 1)
        self.invmod[n] = pow(self.fac[n], mod - 2, mod)
        for i in range(n, 0, -1):
            self.invmod[i - 1] = (self.invmod[i] * i) % mod

    def calc(self, n, k):  # nCk
        return self.fac[n] * self.invmod[k] % mod * self.invmod[n - k] % mod


def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


n, m = map(int, read().split())
mod = 10 ** 9 + 7
comb = Combination(n + 30)
ans = 1
for v in Counter(prime_decomposition(m)).values():
    ans *= comb.calc(n + v - 1, v)
    ans %= mod
print(ans)
