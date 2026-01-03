import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
MOD = 10 ** 9 + 7

N, M = map(int, input().split())

if abs(N - M) >= 2:
    print (0)
    exit()

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

#以下使い方

c = Factorial(max(N, M) + 2, MOD)

n = c.factorial(N)
m = c.factorial(M)

if (N == M):
    ans = 2 * n * m % MOD
else:
    ans = n * m % MOD

print (ans)