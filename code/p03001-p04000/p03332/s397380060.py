import numpy as np
MOD = 998244353

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

def gcd(a, b):
    if a > b:
        a, b = b, a
    if b % a == 0:
        return a
    return gcd(b % a, a)

N, A, B, K = map(int, input().split())

if A < B:
    A, B = B, A

# n = 2 * min(K // A + 2, N + 1) + 3
n = min((K + A - 1) // A, N) + 1
lcm = A * B // gcd(A, B)
step = lcm // A

c = Factorial(N + 1, MOD).comb #O(N)

def calc(a, b):
    if a > b:
        a, b = b, a #必ずaのほうが小さくなる
    return (c(N, a) * c(N, b)) % MOD


def count(a, b):
    if a <= N and b <= N:
        return calc(a, b)
    return 0

def maike_satrt(step):
    for i in range(step):
        if (K - A * i) % B == 0:
            return i

start = maike_satrt(step)
# print (start, n)
ans = 0
for a in range(start, n, step): #Aの数
    if A * a > K:
        break
    # if (K - A * a) % B != 0:
    #     continue
    b = (K - A * a) // B
    # print ('a=', a, 'b=', b)
    ans += count(a, b)
    ans %= MOD

print (ans)