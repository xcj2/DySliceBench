def framod(n, a=1, mod=10**9+7):
    for i in range(1,n+1):
        a = a * i % mod
    return a


def power(n, r, mod=10**9+7):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod


def comb(n, k, mod=10**9+7):
    if n < k or k < 0:
        result = 0
    else:
        print(n, k)
        a = framod(n, a=1, mod=mod)
        b = framod(k, a=1, mod=mod)
        c = framod(n-k, a=1, mod=mod)
        result = (a * power(b, mod-2, mod) * power(c, mod-2, mod)) % mod
    return result


MOD = 10**9 + 7
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

comb1 = [0]*N
comb1[K-1] = 1
for j in range(K+1, N+1):
  comb1[j-1] = comb1[j-2]*(j-1)*power(j-K, MOD-2) % MOD

comb2 = comb1[::-1]
ans = 0
for c1, c2, a in zip(comb1, comb2, A):
  ans = (ans + (c1-c2)*a)%MOD

print(ans)