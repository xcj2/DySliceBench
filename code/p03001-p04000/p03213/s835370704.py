import sys, math
from collections import defaultdict
def input(): return sys.stdin.readline().strip()


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit < p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


def main():
    N = int(input())
    if N < 10:
        print(0)
        return
    table = get_sieve_of_eratosthenes(N)
    #print(table)
    primes = defaultdict(int)
    for n in range(2, N + 1):
        for p in table:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            primes[p] += cnt
    #print(primes)
    
    over_3 = 0
    over_5 = 0
    over_15 = 0
    over_25 = 0
    over_75 = 0
    for p in primes:
        if primes[p] >= 2: over_3 += 1
        if primes[p] >= 4: over_5 += 1
        if primes[p] >= 14: over_15 += 1
        if primes[p] >= 24: over_25 += 1
        if primes[p] >= 74: over_75 += 1
    #print(over_3)
    #print(over_5)
    #print(over_15)
    #print(over_25)
    #print(over_75)
    
    val1 = over_5 * (over_5 - 1) * (over_3 - 2) // 2
    val2 = over_15 * (over_5 - 1)
    val3 = over_25 * (over_3 - 1)
    print(val1 + val2 + val3 + over_75)

    




if __name__ == "__main__":
    main()
