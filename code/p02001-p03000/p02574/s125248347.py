def main():
    from math import gcd
    MINFact = [-1] * (10**6 + 10)
    MINFact[0] = 0
    MINFact[1] = 1

    def Eratosthenes(sup: int) -> set:
        primes = [True for i in range(sup+1)]
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

    _ = int(input())
    A = [int(i) for i in input().split()]
    g = A[0]
    for a in A:
        g = gcd(g, a)
    Eratosthenes(10**6 + 5)
    B = [0]*(10**6 + 5)
    for a in A:
        prime_factor(a)
    # 素因数分解したのをBにいれる
    # 1より大きいのがあったら gcd != 1 のペアが存在する
    if g != 1:
        print("not coprime")
    elif max(B) <= 1:
        print("pairwise coprime")
    else:
        print("setwise coprime")


if __name__ == '__main__':
    main()
