MOD = 10 ** 9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

def init(n):
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        factinv.append((factinv[-1] * inv[-1]) % MOD)

def nPk(n, k):
    return fact[n] * factinv[n - k] % MOD

def nCk(n, k):
    return fact[n] * factinv[n - k] * factinv[k] % MOD

K = int(input())
N = len(input())

init(N + K)
p25 = [1]
p26 = [1]

for k in range(K):
    p25.append(p25[-1] * 25 % MOD)
    p26.append(p26[-1] * 26 % MOD)

ans = 0
for m in range(K + 1):
    n = N + K
    ans += p25[K - m] * p26[m] * nCk(n - 1 - m, N - 1) % MOD
print(ans % MOD)
