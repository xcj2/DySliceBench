
MOD = 10 ** 9 + 7

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, K = ZZ()

    fact = [0] * (N + 1) # fact[n] = n!
    ifact = [0] * (N + 1)

    for i in range(N+1):
        if i == 0:
            fact[i] = 1
            continue
        fact[i] = i * fact[i-1]
        fact[i] %= MOD
    ifact[N] = pow(fact[N], MOD-2, MOD)
    for i in range(N)[::-1]:
        ifact[i] = ((i+1) * ifact[i+1])%MOD

    def comb(n, r):
        if r < 0 or r > n: return 0
        return fact[n]*ifact[n-r]*ifact[r]%MOD

    for i in range(1, K+1): print(comb(K-1, i-1) * comb(N-K+1, i) % MOD)

    return

if __name__ == '__main__':
    main()
