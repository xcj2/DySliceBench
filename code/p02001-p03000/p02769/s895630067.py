import sys
input = sys.stdin.readline

MOD = 10**9+7

class Comb:
    def __init__(self, N):
        self.fac = [1] * (N+1)
        for i in range(2, N+1): self.fac[i] = self.fac[i-1] * i % MOD

    def pow(self, a, b):
        res = 1
        while b:
            if b & 1: res = res * a % MOD
            a = a**2 % MOD
            b >>= 1
        return res

    def pow2(self, a, b):
        return pow(a, b, MOD)

    def comb(self, n, r):
        if r < 0 or r > n: return 0
        return (self.fac[n] * self.pow2(self.fac[r], MOD-2)) % MOD * self.pow2(self.fac[n-r], MOD-2) % MOD

    def permutation(self, n, r):
        if r == 0: return 1
        return self.fac[n] * self.pow2(self.fac[n-r], MOD-2) % MOD

def main():
  N, K = list(map(int, input().split()))

  comb = Comb(N)
  ans = 0

  for i in range(min(N, K)+1):
      ans = ans + (comb.comb(N, i) * comb.comb(N-1, i) % MOD)
      ans %= MOD

  print(ans) 

if __name__ == '__main__':
  main()