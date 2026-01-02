import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

class Factorial:
    def __init__(self, n, mod):
        self.f = [1]
        self.mod = mod
        for j in range(1, n + 1):
            self.f.append(self.f[-1] * j % mod)
        self.i = [pow(self.f[-1], mod - 2, mod)]
        for j in range(n, 0, -1):
            self.i.append(self.i[-1] * j % mod)
        self.i.reverse()
    def factorial(self, j):
        return self.f[j]
    def ifactorial(self, j):
        return self.i[j]
    def comb(self, n, k):
        return self.f[n] * self.i[n - k] % self.mod * self.i[k] % self.mod if n >= k else 0

C = Factorial(2 * 10 ** 6 + 5, MOD).comb

r1, c1, r2, c2 = map(int, input().split())

ans = 0
for i in range(c2 - c1 + 1):
    tmp = C(r2 + c2 + 1 - i, r2) - C(r1 + c2 - i, r1 - 1)
    # print (tmp, C(r2 + c2 + 1 - i, r2), C(r1 + c2 - i, r1 - 1))

    ans += tmp
    ans %= MOD

print (ans)
