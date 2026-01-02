N, A, B, K = [int(_) for _ in input().split()]

L = 300000+1
M = 998244353

Fm = {}
inverseFm = {}
x = 1
for i in range(L):
    Fm[i] = x
    x = x * (i + 1) % M

def inverseFm(x, cache={}):
    if x in cache:
        return cache[x]
    result = pow(Fm[x], M - 2, M)
    cache[x] = result
    return result

def C(n, r):
    result = Fm[n] * inverseFm(r) * inverseFm(n - r) % M
    return result

def solve(N, A, B, K):
    result = 0
    for a in range(0, N+1):
        b, m = divmod(K - A * a, B)
        if m == 0 and 0 <= b <= N:
            result += C(N, a) * C(N, b) % M
    return result % M

print(solve(N, A, B, K))
