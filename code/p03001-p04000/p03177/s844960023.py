import sys

n, k = [int(i) for i in sys.stdin.readline().split()]
a_ls = []
MOD = 10**9+7
for i in range(n):
    a_ls.append([int(i) for i in sys.stdin.readline().split()])


def matmul(a, b):
    x = len(a)
    res = [[0 for i in range(x)]for j in range(x)]
    for i in range(x):
        for j in range(x):
            for k in range(x):
                res[i][j] += (a[i][k] * b[k][j])
            res[i][j] %= MOD
    return res

def power(a, n):
    x = len(a)
    res = a
    for i in range(n - 1):
        res = matmul(res, a)
    return res

def plus(a, b):
    x = len(a)
    res = [[0 for i in range(x)]for j in range(x)]
    for i in range(x):
        for j in range(x):
            res[i][j] = (a[i][j] + b[i][j]) % MOD
    return res

k_2 = bin(k)[2:][::-1]
base = a_ls
res = [[1 if i == j else 0 for i in range(n)]for j in range(n)]
for ind, _k in enumerate(k_2):
    if _k == "1":
        res = matmul(res, base)
    base = power(base, 2)
print(sum([sum(i) % MOD for i in res]) % MOD)