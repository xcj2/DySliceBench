#!/usr/bin/env python3
import sys

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [i for i in range(1, n+1) if is_prime[i-1]]
    return table

def solve(Q: int, l: "List[int]", r: "List[int]"):
    primes = sieve(10**5)
    hash_table = {}

    for prime in primes:
        hash_table[prime] = True
    
    like_number_list = []
    for prime in primes:
        if hash_table.get((prime+1)/2) == True:
            like_number_list.append(prime)
    
    ## i以下の最大の2017likenumberの個数
    ruiseki_like_number = [0]*(10**5+1)
    for like in like_number_list:
        ruiseki_like_number[like] += 1

    from itertools import accumulate
    ruiseki_like_number = list(accumulate(ruiseki_like_number))

    for i in range(Q):
        left = ruiseki_like_number[l[i]-1]
        right = ruiseki_like_number[r[i]]
        print(right-left)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(Q, l, r)

if __name__ == '__main__':
    main()
