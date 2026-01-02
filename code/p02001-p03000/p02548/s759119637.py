def main():
    N = int(input())

    class osa_k:
        def __init__(self, sup):
            if sup > 2 * 10**8:
                raise RuntimeError(
                )
            self.MINFact = [-1] * (sup + 1)
            self.MINFact[0] = 0
            self.MINFact[1] = 1
            primes = [True for i in range(sup+1)]
            primes[0] = False
            primes[1] = False
            for i in range(2, sup+1):
                if primes[i]:
                    self.MINFact[i] = i
                    mul = 2
                    while i*mul <= sup:
                        primes[i*mul] = False
                        if self.MINFact[i*mul] == -1:
                            self.MINFact[i*mul] = i
                        mul += 1

        def prime_factor(self, n):
            res = 1
            while n > 1:
                prime = self.MINFact[n]
                exp = 0
                while self.MINFact[n] == prime:
                    n //= prime
                    exp += 1
                res *= (exp + 1)
            return res

    ok = osa_k(N+1)

    ans = 0
    for c in range(1, N):
        M = N - c
        ans += ok.prime_factor(M)
    print(ans)


if __name__ == '__main__':
    main()
