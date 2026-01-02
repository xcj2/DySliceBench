
import math
from functools import reduce


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def eratosthenes(n):
    D = [0]*(n+1)
    for i in range(2, n+1):
        if D[i] > 0:
            continue
        for j in range(i, n+1, i):
            D[j] = i
    return D


N = int(input())
A = list(map(int, input().split()))
D = eratosthenes(10**6+1)
# D = eratosthenes(max(A))
dic = {}
for i in A:
    while i != 1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
        i //= D[i]
isPairwise = True
for i in dic.items():
    if i[1] > 1:
        isPairwise = False
        break


def is_pairwise():
    used_primes = [False] * (10**6 + 1)
    for a in A:
        while a > 1:
            prime = D[a]
            while a % prime == 0:
                a //= prime
            if used_primes[prime]:
                return False
            used_primes[prime] = 1
    return True


# if isPairwise:
if is_pairwise():
    print("pairwise coprime")
elif gcd_list(A) == 1:
    print("setwise coprime")
else:
    print("not coprime")
