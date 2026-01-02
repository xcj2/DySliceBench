#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int
def comb(n, k):
    k = min(n-k,k)
    ans = 1
    for i in range(1, k + 1):
        ans = (ans * (n + 1 - i) // i)
    return ans

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

def solve(N: int, M: int):
    from collections import Counter
    primes = prime_decomposition(M)

    counter = Counter(primes)
    answer = 1
    for count in counter.values():
        answer *= comb(count+N-1,count)
        answer %= MOD
    
    print(answer)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)

if __name__ == '__main__':
    main()
