K, N = map(int, input().split())
MOD = 998244353

P = N+K
fact = [1]*(P+1)
rfact = [1]*(P+1)
for i in range(P):
    fact[i+1] = r = ((i+1) * fact[i]) % MOD
    rfact[i+1] = pow(r, MOD-2, MOD)

def comb(n, k):
    return fact[n] * rfact[k] * rfact[n-k] % MOD

def h(n, k):
    if n < 0 or k < 0:
        return 0
    return comb(n+k, k)

def calc(A):
    M = A//2
    r = 0
    if A % 2:
        p = K - 2*M + N - 2
        for m in range(M+1):
            if K-2*M-2+m < 0 or N-m < 0:
                continue
            r += pow(2, m, MOD) * comb(M, m) * (h(K-2*M-2+m, N-m) + h(K-2*M-2+m, N-m-1)) % MOD
    else:
        p = K - 2*M + N - 1
        for m in range(M+1):
            if K-2*M-1+m < 0 or N-m < 0:
                continue
            r += pow(2, m, MOD) * comb(M, m) * h(K-2*M-1+m, N-m) % MOD
    return r % MOD
ans = []
for i in range(2, 2*K+1):
    if i <= K:
        ans.append(calc(i - 1))
    else:
        ans.append(calc(2*K - i + 1))
print(*ans, sep='\n')