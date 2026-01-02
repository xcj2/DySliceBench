#!/usr/bin/env python3
import sys
from collections import Counter

MOD = 1000000007  # type: int

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = {i:0 for i in range(1, n+1) if is_prime[i-1]}
    # return is_prime, table
    return table

def prime_decomposition(n):
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n //= i
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table

def solve(N: int, A: "List[int]"):
    table = dict()

    for i in range(N):
        decom = Counter(prime_decomposition(A[i]))

        for d,number in decom.items():
            if table.get(d) == None:
                table[d] = number
                continue

            if table[d] < number:
                table[d] = number
    LCM = 1
    for key,value in table.items():
        LCM *= pow(key,value,MOD)

    print(sum([LCM*pow(a,MOD-2,MOD) for a in A])%MOD)

    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
