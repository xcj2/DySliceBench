#!/usr/bin/env python3
import numpy as np


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def seachPrimeNum(N):
    max = int(np.sqrt(N))
    seachList = [i for i in range(2, N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


def prime3(n):
    counter = 0
    primes = [2, 3]

    for n in range(5, n, 2):
        isprime = True
        for i in range(1, len(primes)):
            counter += 1
            if primes[i] ** 2 > n:
                break
            counter += 1
            if n % primes[i] == 0:
                isprime = False
                break
        if isprime:
            primes.append(n)
    return primes

a,b=map(int,input().split())
# a=b=10**10
count=0
ad=set(make_divisors(a))
bd=set(make_divisors(b))
# print(ad)
common=ad & bd
# print(common)
l=[]
for s in common:
    if is_prime(s):
        count+=1
print(count+1)
# pr=set(seachPrimeNum(max(common)))
# ans=common & pr 
# print(ans)
# print(len(ans)+1)

