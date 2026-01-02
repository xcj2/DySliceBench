import sys, math
from collections import defaultdict
def input(): return sys.stdin.readline().strip()
mod = 10**9+7

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

def factorization(n):
    if n == 1: print("n must be > 1")
    arr = []
    temp = n
    for i in range(2, int(round(n ** 0.5))+1):
        cnt = 0
        while temp % i == 0:
            cnt += 1
            temp //= i
        if cnt > 0: arr.append([i, cnt])
    if temp != 1: arr.append([temp, 1])
    if arr == []: arr.append([n, 1])
    return arr


def main():
    comb = Combination(10**6)
    N, M = map(int, input().split())
    if M == 1:
        print(1)
        return
        
    primes = factorization(M)
    ans = 1
    for _, num in primes:
        ans *= comb(num + (N - 1), num)
        ans %= mod
    print(ans)





if __name__ == "__main__":
    main()
