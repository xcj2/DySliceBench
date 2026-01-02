def main():

    import sys
    input = lambda: sys.stdin.readline().rstrip("\r\n")

    from math import gcd

    def prime_factorize(n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

    n = int(input())
    a = [int(x) for x in input().split()]

    primes = set()

    flag = 1

    for i in a:
        prime_factors = set(prime_factorize(i))
        for j in prime_factors:
            if j in primes:
                flag = 0
            else:
                primes.add(j)


    if flag:
        print('pairwise coprime')
        sys.exit()
                
    
    import math
    from functools import reduce
    
    def gcd(*numbers):
        return abs(reduce(math.gcd, numbers))
    
    if gcd(*a) == 1:
        print('setwise coprime')
    else:
        print('not coprime')

main()