def main():
    from math import gcd
    _ = int(input())
    A = [int(i) for i in input().split()]

    class osa_k:
        def __init__(self, sup):
            if sup > 2 * 10**8:
                raise RuntimeError("too big")
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

        def prime_factor(self, n, B):
            while n > 1:
                prime = self.MINFact[n]
                while self.MINFact[n] == prime:
                    n //= prime
                B[prime] += 1

    maxA = max(A)
    p = osa_k(maxA)
    B = [0] * (maxA + 1)
    for a in A:
        p.prime_factor(a, B)

    g = A[0]
    for a in A:
        g = gcd(g, a)

    if g != 1:
        print("not coprime")
    elif max(B) <= 1:
        print("pairwise coprime")
    else:
        print("setwise coprime")


if __name__ == '__main__':
    main()
