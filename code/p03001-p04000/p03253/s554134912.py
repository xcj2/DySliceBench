class Factorials:
    def __init__(self, n=10**6, mod=10**9 + 7):
        self.mod = mod

        # self.fac[i] ≡ i! (factorial:階乗)
        self.fac = [1]
        num = 1
        for i in range(1, n+1):
            num *= i
            num %= mod
            self.fac.append(num)

        # self.rec[i] ≡ 1 / i! (reciprocal:逆数)
        num = pow(num, mod-2, mod)
        self.rec = [1 for i in range(n+1)]
        self.rec[n] = num
        for i in range(n-1, 0, -1):
            num *= i + 1
            num %= mod
            self.rec[i] = num

    # comb(n, r) ≡ nCr
    def comb(self, n, r):
        return self.fac[n] * self.rec[r] * self.rec[n - r] % self.mod
    
    # perm(n, r) ≡ nPr
    def perm(self, n, r):
        return self.fac[n] * self.rec[n-r] % self.mod

    # fact(n) ≡ n!
    def fact(self, n):
        return self.fac[n]

def main():
    mod = 10**9 + 7
    n, m = map(int, input().split())

    if m == 1:
        print(1)
        exit()

    factors = []
    for i in range(2, m+1):
        if i * i > m:
            if m > 1:
                factors.append(1)
            break

        if m % i == 0:
            num = 1
            m //= i
            while m % i == 0:
                num += 1
                m //= i
            factors.append(num)

    fct = Factorials(n=n+max(factors), mod=mod)

    ans = 1
    for i in factors:
        ans *= fct.comb(n+i-1, i)
        ans %= mod

    print(ans)

main()