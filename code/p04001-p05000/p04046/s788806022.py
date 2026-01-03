M = 10**9 + 7
L = 200000

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

def solve(H, W, A, B):
    result = 0
    for i in range(B + 1, W + 1):
        result += C(i + H - A - 1 - 1, i - 1) * C(W - i + A - 1, W - i)
    return result % M

H, W, A, B = [int(_) for _ in input().split()]

print(solve(H, W, A, B))
