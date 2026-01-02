def divisors(n):
    res = []
    for d in range(1, int(n**0.5)+1):
        if n%d==0:
            res.append(d)
            res.append(n//d)
    res = sorted(set(res))
    return res

# 素因数分解
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

def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

N, K = map(int, input().split())
invK = modinv(K)
P = [0] * (K+1)
mod = 10**9+7
for i in range(1, K+1):
    p = pow(K//i * invK, N, mod)
    P[i] = p
KN = pow(K, N, mod)
ans = 0


# https://kazuma8128.hatenablog.com/entry/2018/07/29/231819
for i in range(K, 1, -1):
    #print(i, divisors(i))
    for d in divisors(i):
        if d!=i:
            P[d] -= P[i]
for i, p in enumerate(P[1:], 1):
    n = p * KN % mod
    #print(i, n)
    ans = (ans + n * i) % mod
print(ans)
