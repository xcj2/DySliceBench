import sys
input=sys.stdin.readline

def main():
    N, M, K = list(map(int, input().split()))

    MOD = 998244353

    class Comb:
        def __init__(self, N):
            self.fac = [1] * (N+1)
            for i in range(2, N+1): self.fac[i] = self.fac[i-1] * i % MOD

        def __call__(self, n, r):
            return self.comb(n, r)

        def comb(self, n, r):
            if r < 0 or r > n: return 0
            return (self.fac[n] * pow(self.fac[r], MOD-2, MOD)) % MOD * pow(self.fac[n-r], MOD-2, MOD) % MOD

        def permutation(self, n, r):
            if r == 0: return 1
            return self.fac[n] * pow(self.fac[n-r], MOD-2, MOD) % MOD

    comb = Comb(N)

    ans = 0

    for i in range(K+1):
        n = (comb(N-1, i) * M) % MOD * pow(M-1, N-1-i, MOD) % MOD
        ans += n
        ans %= MOD

    print(ans)

if __name__ == '__main__':
    main()
