def main():
    from math import gcd
    _ = int(input())
    A = [int(i) for i in input().split()]
    maxA = max(A)

    def Eratosthenes(sup: int) -> set:
        primes = [True]*(sup+1)
        primes[0] = False
        primes[1] = False
        for i in range(2, sup+1):
            if primes[i]:
                MINFact[i] = i
                mul = 2
                while i*mul <= sup:
                    primes[i*mul] = False
                    if MINFact[i*mul] == -1:
                        MINFact[i*mul] = i
                    mul += 1

    def prime_factor(n):
        while n != 1:
            prime = MINFact[n]
            while MINFact[n] == prime:
                n //= prime
            B[prime] += 1

    MINFact = [-1] * (maxA + 1)
    MINFact[0] = 0
    MINFact[1] = 1
    Eratosthenes(maxA)

    g = A[0]
    for a in A:
        g = gcd(g, a)

    B = [0]*(maxA+1)
    for a in A:
        prime_factor(a)

    if g != 1:
        print("not coprime")
    elif max(B) <= 1:
        print("pairwise coprime")
    else:
        print("setwise coprime")


if __name__ == '__main__':
    main()
