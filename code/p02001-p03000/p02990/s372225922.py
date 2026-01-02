N, K = map(int, input().split())
m = 10**9 + 7
n = N


# nの階乗をmod mで返す
def mod_factorial(n, m):
    r = 1
    for i in range(1, n+1):
        r *= i
        r %= m
    return r


invs = [0] * (n + 1)
invs[1] = 1
for i in range(2, n + 1):
    invs[i] = m - invs[m % i] * (m // i) % m


# n1とn2のmod での階乗の逆元を返す関数
def mod_inv_factorial2(n1, n2, m):
    n = max(n1, n2)
    r1 = r2 = 1
    for i in range(1, n+1):
        r1 *= invs[i]
        r1 %= m
        if i == min(n1, n2):
            r2 = r1
    return r1*r2 % m


def solver(i):
    return mod_factorial(N-K+1, m)*mod_factorial(K-1, m)*mod_inv_factorial2(i, N-K+1-i, m)*mod_inv_factorial2(i-1, K-i, m)


for i in range(1, K+1):
    if N-K+1-i >= 0:
        print(solver(i) % m)
    else:
        print(0)


