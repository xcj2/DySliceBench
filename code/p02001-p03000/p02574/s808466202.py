import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

n = int(input())
a = [int(x) for x in input().split()]

# 1~aの最大値までの数の最小の素因数を前処理で求める(O(max_aloglog(max_a)))
def smallest_prime_factors(a):
    max_a = max(a)
    smallest_prime_factors = [int(x) for x in range(max_a + 1)]
    for i in range(2, max_a + 1):
        if smallest_prime_factors[i] == i:
            for j in range(i, max_a + 1, i):
                if smallest_prime_factors[j] == j:
                    smallest_prime_factors[j] = i
        else:
            continue
    return smallest_prime_factors

smallest_prime_factors = smallest_prime_factors(a)

# nを素因数分解(O(log(n)))
def prime_factorize(n):
    prime_factors = []
    if n == 1:
        return prime_factors
    while n != smallest_prime_factors[n]:
        prime_factors.append(smallest_prime_factors[n])
        n //= smallest_prime_factors[n]
    prime_factors.append(n)
    return prime_factors

prime_factors = set()

flag = 1

for i in a:
    prime_factorize_i = set(prime_factorize(i))
    for j in prime_factorize_i:
        if j in prime_factors:
            flag = 0
            break
        else:
            prime_factors.add(j)

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