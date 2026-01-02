class Combination:
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def make_factorial_list(self, n):

        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv


def main():
    N,K = map(int,input().split())
    A = [int(x) for x in input().split()]
    A = sorted(A,reverse=True)
    comb = Combination(10**5)
    ans = 0
    for i in range(0,N-K+1):
        ans += A[i]*comb((N-1)-i,K-1)
        ans %= 10**9+7
    for i in range(K-1,N):
        ans -= A[i]*comb(i,K-1)
        ans %= 10**9+7

    print(ans)
if __name__ == '__main__':
    main()