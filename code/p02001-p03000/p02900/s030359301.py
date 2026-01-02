from itertools import chain

from math import sqrt
from collections import Counter

def prime_factorization(n):
    counter = Counter()
    for i in range(2, int(sqrt(n)) + 1):
        while n % i == 0:
            n //= i
            counter[i] += 1
    
    if n != 1:
        counter[n] += 1

    return counter.items()

def get_prime_facts(n):
    return set(map(lambda x: x[0], prime_factorization(n)))

def solution(A, B):
    s = get_prime_facts(A) & get_prime_facts(B) | {1}
    return len(s)

if __name__ == '__main__': 
    A, B = map(int, input().split())
    a = solution(A, B)

    print(a)

