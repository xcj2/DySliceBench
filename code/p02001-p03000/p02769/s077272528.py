class Combination():
    def __init__(self, N:int, P:int):
        self.N = N
        self.P = P
        self.fact = [1, 1]   
        self.factinv = [1, 1]
        self.inv = [0, 1] 

        for i in range(2, N+1):
            self.fact.append((self.fact[-1] * i) % P)
            self.inv.append((-self.inv[P % i] * (P // i)) % P)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % P)
    def getComb(self, n:int, k:int):
        if (k < 0) or (n < k):
            return 0
        k = min(k, n - k)
        return self.fact[n] * self.factinv[k] % self.P * self.factinv[n-k] % self.P

def main():
    n,k = map(int,input().split())
    MOD = 10**9 +7

    COMB = Combination(n,MOD)

    ans = 0
    for i in range(min(n, k+1)):
        ans += COMB.getComb(n,i) * COMB.getComb(n-1,i)
        ans %= MOD

    print(ans)

if __name__ == "__main__":
    main()