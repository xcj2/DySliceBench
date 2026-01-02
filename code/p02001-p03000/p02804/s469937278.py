N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

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

F = Factorial(N + 1, MOD).comb

tmp = 0

if K == 1:
    print (0)
    exit()

lst = [0] * N
K -= 1
for i in range(K, N):
    tmp += F(i - 1, K - 1)
    tmp %= MOD
    lst[i] = tmp

# print (lst)

ans = 0
for a, tmp in zip(A, lst):
    ans += a * tmp
    ans %= MOD

for index, a in enumerate(A):
    if N - 1 - index < 0:
        break
    ans -= a * (F(N - 1 - index, K))
    ans %= MOD

print (ans)