from math import gcd
from functools import reduce

def gcd_list(A):
    return reduce(gcd, A)

def primes(n):
    is_prime = [False] * 2 + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1): # 素数候補
        if not is_prime[i]: continue
        for j in range(2 * i, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def pairwise_coprime(a):
    max_a = max(a)
    in_a = [False] * (max_a + 1)
    for num in a:
        if num >= 2 and in_a[num]:
            return False
        in_a[num] = True

    ps = primes(max_a)  # max(a)以下の素数

    for p in ps:
        cnt = 0
        for i in range(p, max_a + 1, p):
            if in_a[i]:
                cnt += 1
            if cnt > 1:
                return False

    return True



n = int(input())
a = [int(x) for x in input().split()]

if gcd_list(a) == 1:  # setwise coprime or pairwise coprime
    if pairwise_coprime(a):
        print('pairwise coprime')
    else:
        print('setwise coprime')
else:
    print('not coprime')